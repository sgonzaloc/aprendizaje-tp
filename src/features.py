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
    headers = list(headers)
    with open('trained/headers.json', 'w') as outfile:
        json.dump(headers, outfile)


def list_of_headers_load(df):
    try:
        headers = json.load(open('trained/headers.json'))
    except (OSError, IOError):
        list_of_headers_dump(df)
        headers = json.load(open('trained/headers.json'))
    return headers


def features(df_emails):
    df_columns = ['class']
    try:
        df = pd.read_csv('trained/features.pandas') # tal vez falta , encoding='utf-8'
    except IOError:
        df = pd.DataFrame(df_emails, columns=['class'])
    add_feature_len(df_emails, df, df_columns)
    add_feature_count_spaces(df_emails, df, df_columns)
    add_feature_char_count(df_emails, df, df_columns)
    emails_by_headers = get_emails_by_headers(df_emails)
    add_feature_response_mail(emails_by_headers, df, df_columns)
    add_feature_email_headers(emails_by_headers, df, df_columns)
    add_feature_subject_most_common_words_spam(emails_by_headers, df, df_columns)
    add_feature_subject_most_common_words_ham(emails_by_headers, df, df_columns)
    df.to_pandas('trained/features.pandas') # tal vez falta , encoding='utf-8'
    #df = df.loc[:, df_columns]
    return df


def add_feature_subject_most_common_words_spam(emails_by_headers, df, df_columns):
    word_frequencies_spam, word_frequencies_ham = get_subject_most_common_words(df, emails_by_headers)
    most_common_words_spam = [w for (w, f) in word_frequencies_spam][:300]
    most_common_words_ham = [w for (w, f) in word_frequencies_ham][:3000]
    most_common_words = [w for w in most_common_words_spam if w not in most_common_words_ham]

    first_most_common_words = most_common_words[0]
    if unicode.encode(first_most_common_words) not in df.columns.values:
        counter_vector = CountVectorizer(stop_words='english')
        email_subjects_all = [s if (s is not None) else "" for s in list(emails_by_headers['subject'])]
        matrix_all = counter_vector.fit_transform(email_subjects_all)
        for word in most_common_words:
            idx = counter_vector.vocabulary_.get(word)
            word_frequencies_all = matrix_all.getcol(idx).toarray()[:, 0]
            word_key = u''.join((word, u'subject', u'spam'))
            df[word_key] = [int(freq > 0) for freq in word_frequencies_all]
        #df.to_csv('trained/features.csv', index=False, encoding='utf-8')
    df_columns += most_common_words


def add_feature_subject_most_common_words_ham(emails_by_headers, df, df_columns):
    word_frequencies_spam, word_frequencies_ham = get_subject_most_common_words(df, emails_by_headers)
    most_common_words_ham = [w for (w, f) in word_frequencies_ham][:300]
    most_common_words_spam = [w for (w, f) in word_frequencies_spam][:3000]
    most_common_words = [w for w in most_common_words_ham if w not in most_common_words_spam]

    first_most_common_words = most_common_words[0]
    if unicode.encode(first_most_common_words) not in df.columns.values:
        counter_vector = CountVectorizer(stop_words='english')
        email_subjects_all = [s if (s is not None) else "" for s in list(emails_by_headers['subject'])]
        matrix_all = counter_vector.fit_transform(email_subjects_all)
        for word in most_common_words:
            idx = counter_vector.vocabulary_.get(word)
            word_frequencies_all = matrix_all.getcol(idx).toarray()[:, 0]
            word_key = word + '-subject' + '-ham'
            df[word_key] = [int(freq > 0) for freq in word_frequencies_all]
        #df.to_csv('trained/features.csv', index=False, encoding='utf-8')
    df_columns += most_common_words


def add_feature_len(d_emails, df, df_columns):
    if 'len' not in df.columns.values:
        df['len'] = list(map(len, d_emails['text']))
        #df.to_csv('trained/features.csv', index=False, encoding='utf-8')
    df_columns.append('len')


def add_feature_count_spaces(d_emails, df, df_columns):
    if 'count_spaces' not in df.columns.values:
        df['count_spaces'] = list(map(count_spaces, d_emails['text']))
        #df.to_csv('trained/features.csv', index=False, encoding='utf-8')
    df_columns.append('count_spaces')


def add_feature_response_mail(emails_by_headers, df, df_columns):  # dice si el mail es respuesta de otro o no
    if 're:' not in df.columns.values:
        df['re:'] = list(map(lambda s: False if (s is None) else ('re:' in s), emails_by_headers['subject']))
        #df.to_csv('trained/features.csv', index=False, encoding='utf-8')
    df_columns.append('re:')


def add_feature_email_headers(emails_by_headers, df, df_columns):
    first_email_header = unicode.encode(emails_by_headers.keys()[0]) # el indice [0] de esta linea tampoco me funcionaba
    if first_email_header not in df.columns.values:
        for feature in emails_by_headers.keys():
            df[feature] = list(map(lambda x: x is not None, emails_by_headers[feature]))
        #df.to_csv('trained/features.csv', index=False, encoding='utf-8')
    df_columns += emails_by_headers.keys()


def add_feature_char_count(df_emails, df, df_columns):
    if '{' not in df.columns.values:
        char_counter(df_emails, df, df_columns)


def get_emails_by_headers(df_raw):
    try:
        emails_by_headers = json.load(open('trained/emails_by_headers.json'))
    except (OSError, IOError):
        headers = list_of_headers_load(df_raw)
        emails_by_headers = {}
        for mail in df_raw['text']:
            msg = email.message_from_string(mail.encode('utf-8'))
            for header in headers:
                try:
                    emails_by_headers[header].append(msg[header])
                except KeyError:
                    emails_by_headers[header] = [msg[header]]
        with open('trained/emails_by_headers.json', 'w') as outfile:
            json.dump(emails_by_headers, outfile)
    return emails_by_headers


def get_subject_most_common_words(df, emails_by_headers):
    try:
        word_frequencies_spam = json.load(open('trained/subject_most_common_words_spam.json'))
        word_frequencies_ham = json.load(open('trained/subject_most_common_words_ham.json'))
    except (OSError, IOError):
        counter_vector = CountVectorizer(stop_words='english')
        email_subjects_by_class = zip(list(emails_by_headers['subject']), list(df['class']))
        email_subjects_by_class = [(s, c) if (s is not None) else ("", c) for (s, c) in email_subjects_by_class]
        email_subjects_spam = [s for (s, c) in email_subjects_by_class if (c == 'spam')]
        matrix_spam = counter_vector.fit_transform(email_subjects_spam)
        word_frequencies_spam = [(word, matrix_spam.getcol(idx).count_nonzero()) for word, idx in
                                 list(counter_vector.vocabulary_.items())] # Esta linea necesita la ultima version de scikit-learn
        word_frequencies_spam = sorted(word_frequencies_spam, key=lambda x: -x[1])

        email_subjects_ham = [s for (s, c) in email_subjects_by_class if (c == 'ham')]
        matrix_ham = counter_vector.fit_transform(email_subjects_ham)
        word_frequencies_ham = [(word, matrix_ham.getcol(idx).count_nonzero()) for word, idx in
                                list(counter_vector.vocabulary_.items())]
        word_frequencies_ham = sorted(word_frequencies_ham, key=lambda x: -x[1])

        with open('trained/subject_most_common_words_spam.json', 'w') as outfile:
            json.dump(word_frequencies_spam, outfile)
        with open('trained/subject_most_common_words_ham.json', 'w') as outfile:
            json.dump(word_frequencies_ham, outfile)
    return word_frequencies_spam, word_frequencies_ham


def char_counter(df_emails, df, df_columns):
    """
    cuenta aparicion de caracteres raros y
    devuelve un diccionario con llaves q son los caracteres
    y cada llave tiene una lista de la longitud del indice del df con las cuentas
    """
    characters = set(r'!"#$%&\'()*+,-./:;?@[]^_`{|}~')
    try:
        charac_count = json.load(open('trained/charac_count.json'))
    except (OSError, IOError):
        charac_count = {}
        for character in characters:
            charac_count[character] = []

        for mail in df_emails['text']:
            msg = email.message_from_string(mail.encode('utf-8'))
            if not msg.is_multipart():
                body = msg.get_payload()
                total_count = Counter(body)
                for character in characters:
                    charac_count[character].append(total_count[character])
            else:
                for character in characters:
                    charac_count[character].append(0)
        with open('trained/charac_count.json', 'w') as outfile:
            json.dump(charac_count, outfile)

    for character in characters:
        df[character] = charac_count[character]
    df_columns += characters
