% x = [110, 330, 551, 771, 991];
% accuracy_score = [0.99037499, 0.9895, 0.98955555, 0.98983332, 0.98930555];
% std_accuracy = [0.00100930750364, 0.00137939701029, 0.000726498451822, 0.00177297281243, 0.00146857651367]
% f1_score = [0.99037423, 0.98950663, 0.98955478, 0.98983063, 0.9893059];
% std_f1 = [0.00100046189538, 0.00137229917441, 0.000729085614726, 0.00177835783241, 0.00147254143643]
% precision = [0.99055873, 0.98896142, 0.98961196, 0.99002582, 0.98922428];
% std_prec = [0.00228262561321, 0.00223335671302, 0.00115466838027, 0.0018410987262, 0.00132496601677]
% recall_score = [0.99019444, 0.99005556, 0.9895, 0.98963889, 0.98938887];
% std_rec= [0.00118537742108, 0.00136535962823, 0.00144764517199, 0.00250632672309, 0.00197515284626]

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% title('Decision Tree')
% xlabel('Profundidad')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')
% xlim([100 1000])

% x = [1, 3, 5, 7, 9, 11];
% accuracy_score = [0.895625, 0.88565279, 0.87670832, 0.86911111, 0.86423611, 0.85968055];
% std_accuracy = [0.00262145669161, 0.00289412118594, 0.00339359266465, 0.00292736865169, 0.00359733116531, 0.0038359863405]
% f1_score = [0.89691254, 0.88703656, 0.87804756, 0.87049834, 0.86562616, 0.86114928];
% std_f1 = [0.00264731329699, 0.0029989642276, 0.0036709365593, 0.00306940067414, 0.00380045691495, 0.0038586554225]
% precision = [0.88598988, 0.87641978, 0.86856674, 0.86135604, 0.8568255, 0.85223506];
% std_prec = [0.00395489440006, 0.00368357761444, 0.00344441018876, 0.00332508526664, 0.00364475870806, 0.00455104815909]
% recall_score = [0.90813888, 0.89794444, 0.88777778, 0.8798611, 0.87463889, 0.87027777];
% std_rec= [0.00509334711321, 0.0056344481913, 0.00712651322468, 0.00539954696322, 0.00644186194907,0.00559981624485]

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% xlim([0 12])
% title('KNN')
% xlabel('K')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')


% x = [2,5,10,15,20];
% accuracy_score = [0.98831942,0.99318054,0.99354167,0.99476389,0.99466667];
% std_accuracy = [0.00128567940934,0.0007567728354,0.00131209526411,0.00085174941673,0.000896236163129];
% f1_score = [0.98822403,0.99316975,0.9935234,0.99475606,0.99465519];
% std_f1 = [0.00130278356917,0.000758779544071,0.00131740186959,0.000855171312896,0.00089993904288];
% precision = [0.99630139,0.9947361,0.99628514,0.99618469,0.99673701];
% std_prec = [0.00093285278844,0.00133981195696,0.00119810758131,0.000983313962527,0.000870059944429];
% recall_score = [0.9802778,0.9916111,0.99077777,0.99333333,0.99258335];
% std_rec= [0.00190839584259,0.00146354297033,0.00169331576267,0.00152144911453,0.00147013174461];

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% xlim([0 22])
% title('Random Forest')
% xlabel('Cantidad de árboles')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')


x = 1:6;
accuracy_score = [0.99354167,0.99345834,0.99370834,0.99380556,0.99390278,0.99336111];
std_accuracy = [0.00131209526411,0.000877196467389,0.000889423242557,0.000819788515655,0.00111535616894,0.00090393911681];
f1_score = [0.9935234,0.99343898,0.99369153,0.99378794,0.99388793,0.99334477];
std_f1 = [0.00131740186959,0.000881913715507,0.000893236695451,0.000823707722678,0.00111929645407,0.000907869840946];
precision = [0.99628514,0.99634043,0.99631485,0.99659393,0.99626071,0.99575803];
std_prec = [0.00119810758131,0.000875686437088,0.000992884364113,0.00120388594564,0.00112864146251,0.000970140949605];
recall_score = [0.99077777,0.99055554,0.99108334,0.991,0.99152777,0.99094446];
std_rec= [0.00169331576267,0.00139443536975,0.00139137657246,0.00149691658418,0.00160176455576,0.00140106163476];

hold on
plot(x,accuracy_score, '-r*')
set(gca, 'XTick',1:6, 'XTickLabel',{'Sqrt' 'None' 'Auto' '0.1' '0.5' '0.8'})
plot(x,f1_score, 'b--o')
set(gca, 'XTick',1:6, 'XTickLabel',{'Sqrt' 'None' 'Auto' '0.1' '0.5' '0.8'})
plot(x,precision, 'g')
set(gca, 'XTick',1:6, 'XTickLabel',{'Sqrt' 'None' 'Auto' '0.1' '0.5' '0.8'})
plot(x,recall_score, 'm-o')
set(gca, 'XTick',1:6, 'XTickLabel',{'Sqrt' 'None' 'Auto' '0.1' '0.5' '0.8'})
errorbar(x,accuracy_score, std_accuracy, '-r*')
set(gca, 'XTick',1:6, 'XTickLabel',{'Sqrt' 'None' 'Auto' '0.1' '0.5' '0.8'})
errorbar(x,f1_score, std_f1, 'b--o')
set(gca, 'XTick',1:6, 'XTickLabel',{'Sqrt' 'None' 'Auto' '0.1' '0.5' '0.8'})
errorbar(x,precision, std_prec, 'g')
set(gca, 'XTick',1:6, 'XTickLabel',{'Sqrt' 'None' 'Auto' '0.1' '0.5' '0.8'})
errorbar(x,recall_score, std_rec, 'm-o')
set(gca, 'XTick',1:6, 'XTickLabel',{'Sqrt' 'None' 'Auto' '0.1' '0.5' '0.8'})
hold off

%xlim([0 22])
title('Random Forest')
xlabel('Cantidad de atributos')
ylabel('porcentaje (%)')
legend('accuracy score','f1 score', 'precision', 'recall score')


% x = [22,44,66,88];
% accuracy_score = [0.96398612,0.99227778 , 0.99270834,0.99302777];
% std_accuracy = [0.00208244650774,0.000915403877859,0.000913395341788,0.0010932566314];
% f1_score = [0.96382441 ,0.99226647,0.99269813, 0.9930228];
% std_f1 = [0.00208178961687,0.000914636790262,0.000916068963616,0.0010940296815];
% precision = [0.96819515,0.99376301,0.99406897, 0.99374334];
% std_prec = [0.00300162165579,0.0017584995476,0.00127624785841,0.00155935423314];
% recall_score = [0.9595,0.99077779,0.99133334,0.99230556];
% std_rec= [0.0025573714564,0.00138219212228,0.00151534276796,0.00149613489713];

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% xlim([20 90])
% title('PCA con RandomTrees')
% xlabel('alpha')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')

% x = [22,44,66,88];
% accuracy_score = [0.93905556,0.98456943,0.98533335,0.98472224];
% std_accuracy = [0.00189091730977,0.00158047038444,0.00240818755177,0.00135656735933];
% f1_score = [0.93929783,0.98457939,0.98534642,0.9847285];
% std_f1 = [0.00189210939803,0.00158459106677,0.00240732872321,0.00135083007296];
% precision = [0.93558345 ,0.98391358,0.9844756 ,0.98435156];
% std_prec = [0.00296833963833,0.00182563020122,0.00275755426529,0.00226507259981];
% recall_score = [0.94305554,0.98524999,0.98622222,0.98511112];
% std_rec= [0.0033425870628,0.00234865946806,0.00271939136271,0.00195708791003];

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% xlim([20 90])
% title('PCA con Decision Tree')
% xlabel('alpha')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')


% x = 1:4;
% accuracy_score = [0.99455555,0.99323611,0.99037499,0.98533335];
% std_accuracy = [0.00114665899573,0.000760856466687,0.00100930750364,0.00240818755177];
% f1_score = [0.99454728,0.99323379,0.99037423, 0.98534642];
% std_f1 = [0.00114808481725, 0.000762693114496,0.00100046189538,0.00240732872321];
% precision = [0.99607279 ,0.99355253,0.99055873,0.9844756];
% std_prec = [0.00145135957533,0.000984655827231,0.00228262561321,0.00275755426529];
% recall_score = [0.99302777,0.99291665,0.99019444,0.98622222];
% std_rec= [0.00137465917234,0.00126228836424,0.00118537742108,0.00271939136271];

% hold on
% plot(x,accuracy_score, '-r*')
% set(gca, 'XTick',1:4, 'XTickLabel',{'Random Forest', 'Random Forest + PCA', 'Decision Tree', 'Decision Tree + PCA'})
% plot(x,f1_score, 'b--o')
% set(gca, 'XTick',1:4, 'XTickLabel',{'Random Forest', 'Random Forest + PCA', 'Decision Tree', 'Decision Tree + PCA'})
% plot(x,precision, 'g')
% set(gca, 'XTick',1:4, 'XTickLabel',{'Random Forest', 'Random Forest + PCA', 'Decision Tree', 'Decision Tree + PCA'})
% plot(x,recall_score, 'm-o')
% set(gca, 'XTick',1:4, 'XTickLabel',{'Random Forest', 'Random Forest + PCA', 'Decision Tree', 'Decision Tree + PCA'})
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% set(gca, 'XTick',1:4, 'XTickLabel',{'Random Forest', 'Random Forest + PCA', 'Decision Tree', 'Decision Tree + PCA'})
% errorbar(x,f1_score, std_f1, 'b--o')
% set(gca, 'XTick',1:4, 'XTickLabel',{'Random Forest', 'Random Forest + PCA', 'Decision Tree', 'Decision Tree + PCA'})
% errorbar(x,precision, std_prec, 'g')
% set(gca, 'XTick',1:4, 'XTickLabel',{'Random Forest', 'Random Forest + PCA', 'Decision Tree', 'Decision Tree + PCA'})
% errorbar(x,recall_score, std_rec, 'm-o')
% set(gca, 'XTick',1:4, 'XTickLabel',{'Random Forest', 'Random Forest + PCA', 'Decision Tree', 'Decision Tree + PCA'})
% hold off

% xlim([0 22])
% title('Comparación entre los mejores clasificadores con y sin reducción')
% xlabel('Clasificador')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')


% x = [110,220,330,440,551,661,771];
% accuracy_score = [0.99306944,0.99323611,0.99322221,0.99322223,0.99295833,0.99288889,0.99322222];
% std_accuracy = [ 0.00123985306323, 0.000760856466687,0.00109677335439,0.000775292975655,0.00118349997554,0.000947711376369, 0.00109150725495];
% f1_score = [ 0.99306279,0.99323379,0.99321613,0.99321761, 0.99295539 ,0.99288681,0.99321819];
% std_f1 = [0.00124002804521,0.000762693114496,0.0010981254355,0.000776867592901,0.00118391403442,0.000946992447119, 0.00109142832422];
% precision = [0.99404746,0.99355253, 0.9941017,0.99388174,0.99335841, 0.99319293, 0.99382807];
% std_prec = [0.00187766198779, 0.000984655827231,0.00130464623941,0.000996876866218,0.00161852672233, 0.00152271763374,0.00156118849858];
% recall_score = [ 0.99208333, 0.99291665,0.99233333,0.99255556, 0.99255555,0.99258333,0.99261113];
% std_rec= [0.00168164886409,0.00126228836424, 0.00136761376423,0.00120314459414,0.00173383628769, 0.0013780230296,0.00140655546357];

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% xlim([100 800])
% title('PCA con Random Tree')
% xlabel('alpha')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')

% x = [110,220,330,440,550,660,770];
% accuracy_score = [0.98494445,0.98279168,0.98254168,0.98143054,0.98275,0.98125001,0.98116668];
% std_accuracy = [0.0013639411624,0.00210218234642,0.0010319948622,0.00222398466236,0.00115503634229,0.00139166345102,0.00177885975771];
% f1_score = [0.98494654,0.98280349,0.98254598,0.98144555,0.98274426,0.98126874,0.98117988];
% std_f1 = [0.00136362448071,0.00209739109679,0.00102002153585,0.0022202976752,0.00116304557452,0.00138987221513,0.00178582692991];
% precision = [0.98481239 ,0.98214222,0.98234696,0.9806713,0.98304573,0.98029282,0.98045054];
% std_prec = [0.00176830611176,0.00280316911791,0.00218900742813,0.00247384428006,0.00107497228899,0.00190248725872,0.00212182645671];
% recall_score = [0.98508334,0.98347222,0.98275,0.98222223,0.98244444,0.98224999,0.98191669];
% std_rec= [0.00178752919372,0.0027195291669,0.00146170499144,0.00221524474045,0.00173383917143,0.00188173381776,0.00284487975192];

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% xlim([100 800])
% title('PCA con Decision Tree')
% xlabel('alpha')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')


% x = [110,330,551,771,991];
% accuracy_score = [0.46404168,0.54323611,0.55286111,0.55641667,0.58526389];
% std_accuracy = [0.0335245404853,0.0302338267105,0.0344464594823,0.0356713644033,0.0315338634611];
% f1_score = [0.39421178,0.47180335,0.47701509,0.46910755,0.54100384 ];
% std_f1 = [0.0638602590063,0.0503365131312,0.0469804522117,0.0713891728601,0.0449470432905];
% precision = [0.4494361,0.55983745,0.57436238,0.57890455,0.6044014];
% std_prec = [0.0533265739843,0.0391739157914,0.0497319502654,0.0450876154575,0.0384248558826];
% recall_score = [0.35266666,0.41202777, 0.40936112,0.39911112,0.49091667];
% std_rec= [0.0695153250117,0.0656961817017,0.0501570193468,0.0874409714,0.0524227922941];

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% xlim([100 1000])
% title('LSA con Decision Tree')
% xlabel('alpha')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')


% x = [110,330,551,771,991];
% accuracy_score = [ 0.4877639,0.54355556,0.52906945,0.5671111,0.63808334];
% std_accuracy = [0.0407403189743,0.0131052807376,0.0118600151133,0.0315674038985,0.0160156144469];
% f1_score = [0.35949244,0.4087064,0.37782182,0.44753547, 0.58332618];
% std_f1 = [0.0631556667526,0.0235258592165,0.0421519650427,0.0535540512334,0.0246103465883];
% precision = [0.47808562,0.58096835,0.55530512,0.61479844,0.68662963];
% std_prec = [0.0612462820781,0.0260699046735,0.0201191413771,0.0524889595618,0.0168431996];
% recall_score = [0.29038889,0.31619445,0.28838888,0.35241667, 0.50752779];
% std_rec= [0.0650721656213,0.0258802048442,0.045111796318,0.0494478858971,0.0305402476695];

% hold on
% plot(x,accuracy_score, '-r*')
% plot(x,f1_score, 'b--o')
% plot(x,precision, 'g')
% plot(x,recall_score, 'm-o')
% errorbar(x,accuracy_score, std_accuracy, '-r*')
% errorbar(x,f1_score, std_f1, 'b--o')
% errorbar(x,precision, std_prec, 'g')
% errorbar(x,recall_score, std_rec, 'm-o')
% hold off

% xlim([100 1000])
% title('LSA con Random Forest')
% xlabel('alpha')
% ylabel('porcentaje (%)')
% legend('accuracy score','f1 score', 'precision', 'recall score')
