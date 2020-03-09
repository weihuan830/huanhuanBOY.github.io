import random
xxrange = [113.9966155, 114.202464]
yyrange = [22.3010341, 22.4458108]

# transfertype = ["Shopping",
# "Food",
# "Transfer",
# "Transportation",
# "Withdraw",
# "Bill",
# "Surplus"]
# data = []
# for i in range(0, 100):
#     x = random.random() * (xxrange[1]-xxrange[0]) + xxrange[0]
#     y = random.random() * (yyrange[1]-yyrange[0]) + yyrange[0]
#     tp = transfertype[random.randint(0, len(transfertype)-1)]
#     data.append({'key':i, 'des':'自动柜员机现金交易ATM', 'money':random.random() * 10000, 'date':'2019-12-'+str(random.randint(0, 30)), 'flowtype': 'out', 'location':[x, y], 'transType': tp})


data = [{ "key": 0, "des": "自动转账THE HKUOS&T", "money": 18110.529885904199, "date": "2019-12-08", "flowtype": "in", "location": [114.124964935541, 22.39095741257258], "transType": "Salary" },
    { "key": 1, "des": "自动转账THE HKUOS&T", "money": 19527.56350804792, "date": "2019-12-18", "flowtype": "in", "location": [114.10943499074487, 22.318815637565436], "transType": "Salary" },
    { "key": 2, "des": "POS转账交易JP-BOC", "money": 501.776179373212, "date": "2019-12-23", "flowtype": "out", "location": [114.10975886024428, 22.323636597663718], "transType": "Transfer" },
    { "key": 3, "des": "自动柜员机现金交易ATM", "money": 84.7930630296837, "date": "2019-12-15", "flowtype": "out", "location": [114.18669557494759, 22.312105636395682], "transType": "Transportation" },
    { "key": 4, "des": "自动柜员机现金交易ATM", "money": 2170.6331116061274, "date": "2019-12-2", "flowtype": "out", "location": [114.11063826639918, 22.42337615117766], "transType": "Food" },
    { "key": 5, "des": "自动转账THE BOC Salary", "money": 18883.2814058757185, "date": "2019-12-10", "flowtype": "in", "location": [114.02435511495781, 22.429889100454144], "transType": "Salary" },
    { "key": 6, "des": "自动柜员机现金交易ATM", "money": 900.6266535245, "date": "2019-12-5", "flowtype": "out", "location": [114.08378884774957, 22.334157920392435], "transType": "Withdraw" },
    { "key": 7, "des": "POS转账交易JP-BOC", "money": 68.102698124234, "date": "2019-12-01", "flowtype": "out", "location": [114.10902468562591, 22.40972242017155], "transType": "Transportation" },
    { "key": 8, "des": "自动柜员机现金交易ATM", "money": 862.007352467552, "date": "2019-12-11", "flowtype": "out", "location": [114.09867044629588, 22.423805271839637], "transType": "Transfer" },
    { "key": 9, "des": "自动柜员机现金交易ATM", "money": 2246.287168816029, "date": "2019-12-12", "flowtype": "in", "location": [114.05305763133094, 22.40680649334982], "transType": "Transfer" },
    { "key": 10, "des": "自动柜员机现金交易ATM", "money": 286.539689935742, "date": "2019-12-05", "flowtype": "out", "location": [114.02105654497133, 22.43303883661301], "transType": "Shopping" },
    { "key": 11, "des": "自动柜员机现金交易ATM", "money": 875.7630008041573, "date": "2019-12-16", "flowtype": "out", "location": [114.17676664120987, 22.40306757972984], "transType": "Shopping" },
    { "key": 12, "des": "POS转账交易JP-BOC", "money": 65.1760615637204, "date": "2019-12-12", "flowtype": "out", "location": [114.11114365627763, 22.337016453343992], "transType": "Transportation" },
    { "key": 13, "des": "自动柜员机现金交易ATM", "money": 778.303593301762, "date": "2019-12-29", "flowtype": "out", "location": [114.07589121661273, 22.31178455784987], "transType": "Investment" },
    { "key": 14, "des": "自动柜员机现金交易ATM", "money": 500.629600422074, "date": "2019-12-05", "flowtype": "out", "location": [114.2005774988862, 22.38654964276744], "transType": "Withdraw" },
    { "key": 15, "des": "POS转账交易JP-BOC", "money": 62.74735391949, "date": "2019-12-22", "flowtype": "out", "location": [114.16524226070193, 22.379222500169053], "transType": "Transportation" },
    { "key": 16, "des": "自动柜员机现金交易ATM", "money": 3402.749863888989, "date": "2019-12-28", "flowtype": "out", "location": [114.01787236591686, 22.338718711702278], "transType": "Shopping" },
    { "key": 17, "des": "自动柜员机现金交易ATM", "money": 51.561246441314, "date": "2019-12-17", "flowtype": "out", "location": [114.11559553612153, 22.380247266254848], "transType": "Transportation" },
    { "key": 18, "des": "自动柜员机现金交易ATM", "money": 1143.8199190490295, "date": "2019-12-02", "flowtype": "out", "location": [114.10463906585585, 22.354836110607717], "transType": "Bill" },
    { "key": 19, "des": "自动柜员机现金交易ATM", "money": 443.400366954652, "date": "2019-12-08", "flowtype": "out", "location": [114.16846907141421, 22.33719818028327], "transType": "Shopping" },
    { "key": 20, "des": "POS转账交易JP-BOC", "money": 1214.579776565509, "date": "2019-12-12", "flowtype": "out", "location": [114.17726546428081, 22.405669360180664], "transType": "Investment" },
    { "key": 21, "des": "自动柜员机现金交易ATM", "money": 330.3575147884203, "date": "2019-12-12", "flowtype": "out", "location": [114.19794927058746, 22.418522652942872], "transType": "Shopping" },
    { "key": 22, "des": "自动柜员机现金交易ATM", "money": 93.614871844627, "date": "2019-12-08", "flowtype": "out", "location": [114.0220139123304, 22.340697018387637], "transType": "Shopping" },
    { "key": 23, "des": "自动柜员机现金交易ATM", "money": 226.82283486785582, "date": "2019-12-17", "flowtype": "out", "location": [114.10732350180892, 22.428831942756222], "transType": "Investment" },
    { "key": 24, "des": "自动柜员机现金交易ATM", "money": 48.983630131318, "date": "2019-12-05", "flowtype": "out", "location": [114.04903471103714, 22.37833526971214], "transType": "Transportation" },
    { "key": 25, "des": "POS转账交易JP-BOC", "money": 5510.976659165203, "date": "2019-12-12", "flowtype": "in", "location": [114.02397701584428, 22.315476843212885], "transType": "Transfer" },
    { "key": 26, "des": "自动柜员机现金交易ATM", "money": 638.8575852230239, "date": "2019-12-12", "flowtype": "out", "location": [114.02454387806664, 22.32783683756422], "transType": "Shopping" },
    { "key": 27, "des": "自动柜员机现金交易ATM", "money": 3588.6618371374234, "date": "2019-12-21", "flowtype": "in", "location": [114.07893197155164, 22.38241848144672], "transType": "Transfer" },
    { "key": 28, "des": "自动柜员机现金交易ATM", "money": 1319.698032219866, "date": "2019-12-10", "flowtype": "out", "location": [114.10985736544004, 22.307838459743575], "transType": "Withdraw" },
    { "key": 29, "des": "自动柜员机现金交易ATM", "money": 8994.13844949807, "date": "2019-12-08", "flowtype": "out", "location": [114.09542776610404, 22.35979098245211], "transType": "Investment" },
    { "key": 30, "des": "自动柜员机现金交易ATM", "money": 2407.9388020571737, "date": "2019-12-09", "flowtype": "out", "location": [114.16583538113493, 22.413591190263034], "transType": "Transfer" },
    { "key": 31, "des": "自动柜员机现金交易ATM", "money": 5217.666841537808, "date": "2019-12-30", "flowtype": "out", "location": [114.06026109269891, 22.334725254475806], "transType": "Bill" },
    { "key": 32, "des": "自动柜员机现金交易ATM", "money": 1820.3244361964398, "date": "2019-12-24", "flowtype": "out", "location": [114.18967733789349, 22.383925600719248], "transType": "Withdraw" },
    { "key": 33, "des": "自动柜员机现金交易ATM", "money": 700.8188507840277, "date": "2019-12-15", "flowtype": "out", "location": [114.06123790132699, 22.340893931011188], "transType": "Withdraw" },
    { "key": 34, "des": "自动柜员机现金交易ATM", "money": 404.69768326992227, "date": "2019-12-06", "flowtype": "out", "location": [114.06760080293526, 22.42154383670313], "transType": "Withdraw" },
    { "key": 35, "des": "自动柜员机现金交易ATM", "money": 495.9492243062724, "date": "2019-12-08", "flowtype": "out", "location": [114.0985306257177, 22.369440830183148], "transType": "Food" },
    { "key": 36, "des": "自动柜员机现金交易ATM", "money": 4787.51593181726, "date": "2019-12-02", "flowtype": "in", "location": [114.1621830336884, 22.334383327348732], "transType": "Transfer" },
    { "key": 37, "des": "自动柜员机现金交易ATM", "money": 417.882196058623, "date": "2019-12-28", "flowtype": "out", "location": [114.19696484442457, 22.422009834604903], "transType": "Shopping" },
    { "key": 38, "des": "自动柜员机现金交易ATM", "money": 46.700409633278, "date": "2019-12-05", "flowtype": "out", "location": [114.13954200608818, 22.327897628813332], "transType": "Transportation" },
    { "key": 39, "des": "自动柜员机现金交易ATM", "money": 4.6261342135585, "date": "2019-12-06", "flowtype": "out", "location": [114.14407703938006, 22.40807828058791], "transType": "Transportation" },
    { "key": 40, "des": "自动柜员机现金交易ATM", "money": 277.903132087258, "date": "2019-12-05", "flowtype": "out", "location": [114.12241450301454, 22.365329247250088], "transType": "Shopping" },
    { "key": 41, "des": "自动柜员机现金交易ATM", "money": 18.9724072323952, "date": "2019-12-13", "flowtype": "out", "location": [114.04665390746636, 22.378778911228398], "transType": "Transportation" },
    { "key": 42, "des": "自动柜员机现金交易ATM", "money": 8.835195917780148, "date": "2019-12-19", "flowtype": "out", "location": [114.00282998839288, 22.309906491192194], "transType": "Food" },
    { "key": 43, "des": "自动柜员机现金交易ATM", "money": 500.0298154911109, "date": "2019-12-10", "flowtype": "out", "location": [114.11340836099073, 22.348045011963286], "transType": "Surplus" },
    { "key": 44, "des": "自动柜员机现金交易ATM", "money": 539.340174071749, "date": "2019-12-22", "flowtype": "out", "location": [114.06103421273062, 22.388968628983818], "transType": "Investment" },
    { "key": 45, "des": "自动柜员机现金交易ATM", "money": 334.8257652595993, "date": "2019-12-09", "flowtype": "out", "location": [114.09120298787944, 22.408934012349143], "transType": "Shopping" },
    { "key": 46, "des": "自动柜员机现金交易ATM", "money": 77.181548516006, "date": "2019-12-26", "flowtype": "out", "location": [113.99914913470415, 22.433179817038322], "transType": "Transportation" },
    { "key": 47, "des": "自动柜员机现金交易ATM", "money": 724.05613820176, "date": "2019-12-16", "flowtype": "out", "location": [114.14130775825245, 22.370196036408053], "transType": "Transfer" },
    { "key": 48, "des": "自动柜员机现金交易ATM", "money": 92.576182044331, "date": "2019-12-03", "flowtype": "out", "location": [114.13934180690218, 22.311198797662488], "transType": "Transportation" },
    { "key": 49, "des": "自动柜员机现金交易ATM", "money": 418.3068944890786, "date": "2019-12-14", "flowtype": "out", "location": [114.1385422086464, 22.3699751682385], "transType": "Food" },
    { "key": 50, "des": "自动柜员机现金交易ATM", "money": 1812.148217452079, "date": "2019-12-16", "flowtype": "out", "location": [114.16781579237275, 22.37921314491031], "transType": "Investment" },
    { "key": 51, "des": "自动柜员机现金交易ATM", "money": 1001.1431513530322, "date": "2019-12-03", "flowtype": "out", "location": [114.0698753151674, 22.443828189892315], "transType": "Investment" },
    { "key": 52, "des": "自动柜员机现金交易ATM", "money": 88.87431144818, "date": "2019-12-08", "flowtype": "out", "location": [114.10852893654219, 22.441613106265176], "transType": "Transportation" },
    { "key": 53, "des": "自动柜员机现金交易ATM", "money": 860.887402574497, "date": "2019-12-28", "flowtype": "out", "location": [114.06560034022127, 22.426091702267236], "transType": "Food" },
    { "key": 54, "des": "自动柜员机现金交易ATM", "money": 4.510334943829, "date": "2019-12-06", "flowtype": "out", "location": [114.03033311733893, 22.327107629041137], "transType": "Transportation" },
    { "key": 55, "des": "自动柜员机现金交易ATM", "money": 539.8478445703086, "date": "2019-12-06", "flowtype": "out", "location": [114.06158152136813, 22.38665732499397], "transType": "Food" },
    { "key": 56, "des": "自动柜员机现金交易ATM", "money": 24.001799072913, "date": "2019-12-14", "flowtype": "out", "location": [114.17833071160325, 22.436108827363018], "transType": "Transportation" },
    { "key": 57, "des": "自动柜员机现金交易ATM", "money": 1148.4706061638738, "date": "2019-12-11", "flowtype": "out", "location": [114.1846876718435, 22.344776454575673], "transType": "Surplus" },
    { "key": 58, "des": "自动柜员机现金交易ATM", "money": 250.010169986141, "date": "2019-12-15", "flowtype": "out", "location": [114.13060311208679, 22.35648698112507], "transType": "Shopping" },
    { "key": 59, "des": "自动柜员机现金交易ATM", "money": 52.6552007146465, "date": "2019-12-07", "flowtype": "out", "location": [114.10750941253589, 22.33461349203547], "transType": "Transportation" },
    { "key": 60, "des": "自动柜员机现金交易ATM", "money": 164.75651544169, "date": "2019-12-03", "flowtype": "out", "location": [114.01872110135608, 22.353194287903648], "transType": "Food" },
    { "key": 61, "des": "自动柜员机现金交易ATM", "money": 4336.749576472541, "date": "2019-12-02", "flowtype": "out", "location": [114.18244146093554, 22.326799035925784], "transType": "Shopping" },
    { "key": 62, "des": "自动柜员机现金交易ATM", "money": 798.208016713332, "date": "2019-12-05", "flowtype": "out", "location": [114.03114702137194, 22.367624608129443], "transType": "Transfer" },
    { "key": 63, "des": "自动柜员机现金交易ATM", "money": 950.505668234944, "date": "2019-12-05", "flowtype": "out", "location": [114.05459270410694, 22.43928343116151], "transType": "Shopping" },
    { "key": 64, "des": "自动柜员机现金交易ATM", "money": 659.645441948668, "date": "2019-12-24", "flowtype": "out", "location": [114.11532411527914, 22.40130403663817], "transType": "Food" },
    { "key": 65, "des": "自动柜员机现金交易ATM", "money": 5154.5864267697525, "date": "2019-12-04", "flowtype": "out", "location": [114.05405404740495, 22.314994034207437], "transType": "Surplus" },
    { "key": 66, "des": "自动柜员机现金交易ATM", "money": 437.939345758666, "date": "2019-12-02", "flowtype": "out", "location": [114.06824787490417, 22.323894099042782], "transType": "Transfer" },
    { "key": 67, "des": "自动柜员机现金交易ATM", "money": 3902.9208336095935, "date": "2019-12-03", "flowtype": "out", "location": [114.04188820144905, 22.352347721338663], "transType": "Surplus" },
    { "key": 68, "des": "自动柜员机现金交易ATM", "money": 2456.281555292839, "date": "2019-12-29", "flowtype": "out", "location": [114.19345594269865, 22.309136824891016], "transType": "Withdraw" },
    { "key": 69, "des": "自动柜员机现金交易ATM", "money": 4593.039291027827, "date": "2019-12-23", "flowtype": "out", "location": [114.05530744661125, 22.325596814811995], "transType": "Investment" },
    { "key": 70, "des": "自动柜员机现金交易ATM", "money": 71.6966538609954, "date": "2019-12-09", "flowtype": "out", "location": [113.99987832515613, 22.428502958577695], "transType": "Transportation" },
    { "key": 71, "des": "自动柜员机现金交易ATM", "money": 601.838691424426, "date": "2019-12-25", "flowtype": "out", "location": [114.04820248428905, 22.370669178679325], "transType": "Food" },
    { "key": 72, "des": "自动柜员机现金交易ATM", "money": 98.4162423777457, "date": "2019-12-08", "flowtype": "out", "location": [114.08442975041253, 22.341425942948046], "transType": "Transportation" },
    { "key": 73, "des": "自动柜员机现金交易ATM", "money": 2688.437846036513, "date": "2019-12-05", "flowtype": "out", "location": [114.10420153306082, 22.30206837084903], "transType": "Investment" },
    { "key": 74, "des": "自动柜员机现金交易ATM", "money": 55.048881931365, "date": "2019-12-25", "flowtype": "out", "location": [114.1056872632041, 22.35524206585802], "transType": "Transportation" },
    { "key": 75, "des": "自动柜员机现金交易ATM", "money": 594.852778494969, "date": "2019-12-19", "flowtype": "out", "location": [114.16227659623367, 22.355056530750847], "transType": "Food" },
    { "key": 76, "des": "自动柜员机现金交易ATM", "money": 216.0383998194837, "date": "2019-12-24", "flowtype": "out", "location": [114.14274102818776, 22.392399738852536], "transType": "Transfer" },
    { "key": 77, "des": "自动柜员机现金交易ATM", "money": 2660.385303071263, "date": "2019-12-30", "flowtype": "out", "location": [114.1085996452204, 22.41369642791409], "transType": "Surplus" },
    { "key": 78, "des": "自动柜员机现金交易ATM", "money": 34.234820417612, "date": "2019-12-30", "flowtype": "out", "location": [114.04969357902917, 22.419992078289326], "transType": "Transportation" },
    { "key": 79, "des": "自动柜员机现金交易ATM", "money": 655.411111498297, "date": "2019-12-19", "flowtype": "out", "location": [114.10851403016143, 22.38002272814942], "transType": "Food" },
    { "key": 80, "des": "自动柜员机现金交易ATM", "money": 24.550852836887, "date": "2019-12-23", "flowtype": "out", "location": [114.08221935452046, 22.316443253860122], "transType": "Transportation" },
    { "key": 81, "des": "自动柜员机现金交易ATM", "money": 284.567477957243, "date": "2019-12-08", "flowtype": "out", "location": [114.17470307984527, 22.35873236928128], "transType": "Food" },
    { "key": 82, "des": "自动柜员机现金交易ATM", "money": 162.603148140148, "date": "2019-12-25", "flowtype": "out", "location": [114.15539318595103, 22.43380315596254], "transType": "Food" },
    { "key": 83, "des": "自动柜员机现金交易ATM", "money": 791.343979976034, "date": "2019-12-02", "flowtype": "out", "location": [114.09021058568635, 22.428921389095485], "transType": "Food" },
    { "key": 84, "des": "自动柜员机现金交易ATM", "money": 2847.7182394725733, "date": "2019-12-05", "flowtype": "out", "location": [114.01296322385754, 22.330593063534288], "transType": "Transfer" },
    { "key": 85, "des": "自动柜员机现金交易ATM", "money": 780.666630613123, "date": "2019-12-11", "flowtype": "out", "location": [114.1047009878777, 22.42216206418022], "transType": "Shopping" },
    { "key": 86, "des": "自动柜员机现金交易ATM", "money": 218.636003176868, "date": "2019-12-10", "flowtype": "out", "location": [114.02817907064406, 22.373958582168445], "transType": "Shopping" },
    { "key": 87, "des": "自动柜员机现金交易ATM", "money": 492.995871467111, "date": "2019-12-09", "flowtype": "out", "location": [114.12127896965902, 22.427410215103556], "transType": "Transfer" },
    { "key": 88, "des": "自动柜员机现金交易ATM", "money": 291.389938810398, "date": "2019-12-16", "flowtype": "out", "location": [113.99667473640876, 22.39960018574876], "transType": "Surplus" },
    { "key": 89, "des": "自动柜员机现金交易ATM", "money": 9224.891562273337, "date": "2019-12-20", "flowtype": "out", "location": [114.03569068649429, 22.32585309599422], "transType": "Surplus" },
    { "key": 90, "des": "自动柜员机现金交易ATM", "money": 1740.086392811553, "date": "2019-12-30", "flowtype": "out", "location": [114.12119635547795, 22.363721176734106], "transType": "Transfer" },
    { "key": 91, "des": "自动柜员机现金交易ATM", "money": 21.645212641948, "date": "2019-12-22", "flowtype": "out", "location": [114.18491261555731, 22.415775862162835], "transType": "Transportation" },
    { "key": 92, "des": "自动柜员机现金交易ATM", "money": 233.045620662756, "date": "2019-12-14", "flowtype": "out", "location": [114.10874957473395, 22.434495708458456], "transType": "Shopping" },
    { "key": 93, "des": "自动柜员机现金交易ATM", "money": 4019.345356835341, "date": "2019-12-13", "flowtype": "in", "location": [114.07729967638566, 22.31294343905039], "transType": "Transfer" },
    { "key": 94, "des": "自动柜员机现金交易ATM", "money": 339.4440456204934, "date": "2019-12-02", "flowtype": "out", "location": [114.06342091674871, 22.341831920871584], "transType": "Food" },
    { "key": 95, "des": "自动柜员机现金交易ATM", "money": 9.0699409357826, "date": "2019-12-25", "flowtype": "out", "location": [114.17837368993135, 22.392901321813866], "transType": "Transportation" },
    { "key": 96, "des": "自动柜员机现金交易ATM", "money": 1111.16550340657163, "date": "2019-12-29", "flowtype": "out", "location": [114.07982255078228, 22.3203868005772], "transType": "Transfer" },
    { "key": 97, "des": "自动柜员机现金交易ATM", "money": 272.6409099307598, "date": "2019-12-05", "flowtype": "out", "location": [114.16743248244686, 22.420030778870643], "transType": "Food" },
    { "key": 98, "des": "自动柜员机现金交易ATM", "money": 20.87318425597, "date": "2019-12-17", "flowtype": "out", "location": [114.01396610518444, 22.39108435438507], "transType": "Transportation" },
    { "key": 99, "des": "自动柜员机现金交易ATM", "money": 230.3428676978425, "date": "2019-12-28", "flowtype": "out", "location": [113.99823882371872, 22.419769252827], "transType": "Food" }
]

{
    "nodes": [
        { "node": 0, "name": "Surplus" },
        { "node": 1, "name": "Salary" },
        { "node": 2, "name": "Fund" },
        { "node": 3, "name": "Stock" },
        { "node": 4, "name": "Savings" },
        { "node": 5, "name": "Investment" },
        { "node": 6, "name": "Shopping" },
        { "node": 7, "name": "Food" },
        { "node": 8, "name": "Transfer" },
        { "node": 9, "name": "Transportation" },
        { "node": 10, "name": "Withdraw" },
        { "node": 11, "name": "Bill" },
        { "node": 12, "name": "Surplus" },
        { "node": 13, "name": "Transfer" }
    ],
    "links": [
        { "source": 0, "target": 4, "value": 3000 },
        { "source": 1, "target": 4, "value": 56521.37 },
        { "source": 4, "target": 6, "value": 13871.50 },
        { "source": 4, "target": 7, "value": 9251.90 },
        { "source": 4, "target": 8, "value": 12139.93 },
        { "source": 4, "target": 9, "value": 1126.99 },
        { "source": 4, "target": 10, "value": 8103.07 },
        { "source": 4, "target": 11, "value": 6361.48 },
        { "source": 4, "target": 12, "value": 22882.67 },
        { "source": 4, "target": 5, "value": 21847.95 },
        { "source": 3, "target": 4, "value": 20000.00 },
        { "source": 3, "target": 5, "value": 100000.00 },
        { "source": 2, "target": 5, "value": 30000.00 },
        { "source": 13, "target": 4, "value":  20152.78}
    ]
}
sm = 0
with open("data.txt", "w+") as f:
    for item in data:
        f.write(item["date"] + "," + str(item['money']) + "\n")
    