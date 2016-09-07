# Aprendizaje Automatico - DC, FCEN, UBA
# Segundo cuatrimestre 2016

import json
import email
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter

def count_spaces(txt):  # cuenta la cantidad de espacios en el cuerpo del mail
    return txt.count(" ")


def list_of_headers_dump(df):  # devuelve una lista con todos los headers que hay en todos los mails
    headers = set()
    for mail in df['text']:
        msg = email.message_from_string(mail.encode('utf-8'))
        headers |= set(msg.keys())
    with open('trained/headers.json', 'w') as outfile:
        json.dump(list(headers), outfile)


def list_of_headers_load(df):
    try:
        headers = json.load(open('trained/headers.json'))
    except (OSError, IOError):
        list_of_headers_dump(df)
        headers = json.load(open('trained/headers.json'))
    return headers


def add_feature_response_mail(mails_tagged, df):  # dice si el mail es respuesta de otro o no
    if 're:' not in df.columns.values:
        df['re:'] = map(lambda subject: False if (subject is None) else ('re:' in subject), mails_tagged['Subject'])


def features(d_emails):
    try:
        df = pd.read_csv('trained/features.csv')
    except IOError:
        df = pd.DataFrame(d_emails, columns=['class'])
    add_feature_len(d_emails, df)
    add_feature_count_spaces(d_emails, df)
    mails_tagged = tag_mails(d_emails)
    add_feature_response_mail(mails_tagged, df)
    add_feature_email_tags(mails_tagged, df)
    add_feature_most_common_words_subject(mails_tagged, df)
    add_feature_char_count(d_emails, df)
    df.to_csv('trained/features.csv', index=False)
    return df


def add_feature_most_common_words_subject(mails_tagged, df):
    try:
        most_common_words_spam = json.load(open('trained/subject_most_common_words_spam.json'))
    except (OSError, IOError):
        counter_vector = CountVectorizer(stop_words='english')
        email_subjects_by_class = zip(list(mails_tagged['subject']), list(df['class']))
        email_subjects_spam = [s for (s, c) in email_subjects_by_class if (s is not None) and (c == 'spam')]
        matrix_spam = counter_vector.fit_transform(email_subjects_spam)
        word_frequencies_spam = [(word, matrix_spam.getcol(idx).sum()) for word, idx in list(counter_vector.vocabulary_.items())]
        word_frequencies_spam = sorted(word_frequencies_spam, key=lambda x: -x[1])

        email_subjects_ham = [s for (s, c) in email_subjects_by_class if (s is not None) and (c == 'ham')]
        matrix_spam = counter_vector.fit_transform(email_subjects_ham)
        word_frequencies_ham = [(word, matrix_spam.getcol(idx).sum()) for word, idx in list(counter_vector.vocabulary_.items())]
        word_frequencies_ham = sorted(word_frequencies_ham, key=lambda x: -x[1])

        most_common_words_spam = [spam_word for spam_word in word_frequencies_spam[:100] if spam_word not in word_frequencies_ham[:1000]]
        with open('trained/subject_most_common_words_spam.json', 'w') as outfile:
            json.dump(most_common_words_spam, outfile)
#
#   for word in most_common_words_spam:
#       df[word] =

    return most_common_words_spam


def add_feature_email_tags(mails_tagged, df):
    first_email_tag = mails_tagged.keys()[0]
    if first_email_tag not in df.columns.values:
        for feature in mails_tagged.keys():
            df[feature] = map(lambda x: x is not None, mails_tagged[feature])


def add_feature_count_spaces(d_emails, df):
    if 'count_spaces' not in df.columns.values:
        df['count_spaces'] = map(count_spaces, d_emails['text'])


def add_feature_len(d_emails, df):
    if 'len' not in df.columns.values:
        df['len'] = map(len, d_emails['text'])

def add_feature_char_count(d_mails, df):
    if '{' not in df.columns.values:
        char_counter(d_mails, df)


def tag_mails(df_raw):
    try:
        mails_tagged = json.load(open('trained/mails_tagged.json'))
    except (OSError, IOError):
        headers = list_of_headers_load(df_raw)
        mails_tagged = {}
        for mail in df_raw['text']:
            msg = email.message_from_string(mail.encode('utf-8'))
            for header in headers:
                try:
                    mails_tagged[header].append(msg[header])
                except KeyError:
                    mails_tagged[header] = [msg[header]]
        with open('trained/mails_tagged.json', 'w') as outfile:
            json.dump(mails_tagged, outfile)
    return mails_tagged

def char_counter(df_raw, df):
    """
    cuenta aparicion de caracteres raros y 
    devuelve un diccionario con llaves q son los caracteres
    y cada llave tiene una lista de la longitud del indice del df con las cuentas
    """
    characters = set(r'!"#$%&\'()*+,-./:;?@[]^_`{|}~')
    charac_count = {}
    for character in characters:
        charac_count[character] = []
    
    for i in df_raw.index:
        msg = email.message_from_string(df_raw['text'][i])
        if not msg.is_multipart():
            body = msg.get_payload()
            total_count = Counter(body)
            for character in characters:
                charac_count[character].append(total_count[character])
        else:
            for character in characters:
                charac_count[character].append(0)

    for character in characters:
        df[character] = charac_count[character]