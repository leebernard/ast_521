# Teff 5777.0 logg 4.44 [Fe/H] 0.0 massStar 1.0 xiT 1.0 HeFe 0.0 CO 0.0 AlfFe 0.0 lineThresh -3.0 voigtThresh -3.0 lambda0 5.88e-05 lambda1 5.9199999999999996e-05 logGamCol 0.5 logKapFudge 0.0 macroV 8.0 rotV 50.0 rotI 90.0 RV 0.0 nInner 2 nOuter 2 ifTiO 1 sampling fine

teffRS = 5777.0 # K
loggRS = 4.44 #log (cm/^2)
log10ZScaleRS = 0.0
xiTRS = 1.0 # (km/s) 
logKapFudgeRS = 0.0
logHeFeRS = 0.0
logCORS = 0.0
logAlphaFeRS = 0.0

numDeps = 48

tauRosRS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
tauRosRS[0] = [\
9.999999999999987e-07, 1.479833198237528e-06, 2.1899062946059137e-06, 3.2406960357871624e-06, 4.795689579154601e-06, 7.0968206476747486e-06, 1.0502110796366661e-05, 1.5541372208032142e-05, 2.299863853961207e-05, 3.4034148825183046e-05, 5.03648633052627e-05, 7.453159674382292e-05, 0.00011029433117916116, 0.00016321721285632738, 0.00024153425010859465, 0.0003574304018221048, 0.0005289373746757308, 0.0007827390868337495, 0.00115832328625471, 0.0017141252532913136, 0.0025366194557577986, 0.0037537736819256025, 0.005554958913183833, 0.008220412614574905, 0.012164839490258518, 0.01800193332891547, 0.026639858572587716, 0.03942254711206796, 0.05833879397552123, 0.08633168407011593, 0.12775649214671145, 0.1890582983690759, 0.2797747463288548, 0.41401995764592286, 0.6126804780573327, 0.9066649113412799, 1.3417128354799128, 1.9855111964445844, 2.9382253839710137, 4.348083467104512, 6.434438263328999, 9.52189535408409, 14.090816855117312, 20.852058572487586, 30.857568527160552, 45.66405432338183, 67.57518355386232, 100.00000000000004\
]
tauRosRS[1] = [\
-13.815510557964275, -13.423581180433374, -13.031651802902472, -12.639722425371572, -12.24779304784067, -11.855863670309768, -11.463934292778866, -11.072004915247966, -10.680075537717064, -10.288146160186162, -9.89621678265526, -9.504287405124359, -9.112358027593459, -8.720428650062557, -8.328499272531655, -7.936569895000754, -7.544640517469852, -7.15271113993895, -6.760781762408049, -6.368852384877147, -5.9769230073462465, -5.5849936298153455, -5.193064252284444, -4.801134874753542, -4.40920549722264, -4.017276119691738, -3.625346742160838, -3.2334173646299362, -2.8414879870990344, -2.4495586095681325, -2.0576292320372325, -1.6656998545063306, -1.2737704769754288, -0.8818410994445269, -0.4899117219136251, -0.09798234438272502, 0.29394703314817683, 0.6858764106790787, 1.0778057882099805, 1.4697351657408806, 1.8616645432717824, 2.2535939208026843, 2.6455232983335843, 3.037452675864488, 3.429382053395388, 3.8213114309262917, 4.213240808457192, 4.605170185988092\
]
tempRS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
tempRS[0] = [\
3641.977618744514, 3685.192353892707, 3731.946392778523, 3779.7993569978817, 3827.932161713779, 3875.86815613015, 3923.3599001296684, 3970.173855390393, 4016.359307549695, 4062.061904084044, 4107.423577097383, 4152.612584756318, 4197.681002854106, 4242.53358642999, 4286.9996392335615, 4330.967385293182, 4374.314208701395, 4417.022242119551, 4459.275969381406, 4501.250481415781, 4543.263692537853, 4585.6962059717425, 4629.081669899166, 4674.43927220611, 4722.232643760059, 4773.517504279279, 4830.881982076065, 4895.1063023501065, 4968.382297134734, 5057.32701307546, 5164.79414569574, 5296.559535726942, 5468.203305136253, 5686.021924379499, 5964.002381552235, 6297.589350472983, 6714.825807912001, 7184.042912894396, 7809.268629918883, 8307.78191986626, 8684.078610875657, 8997.26608384397, 9274.05058905373, 9531.530706607437, 9775.691557192671, 10009.713733980603, 10237.961601309828, 10460.544349457357\
]
tempRS[1] = [\
8.200282114948658, 8.212078002417881, 8.224685197656813, 8.23742620704554, 8.250080030815445, 8.262524956985821, 8.274703683049182, 8.286565165012153, 8.29813112638083, 8.309445981828254, 8.320551244040802, 8.33149295364401, 8.342287509607242, 8.35291591373703, 8.363342382444383, 8.37354621066057, 8.383505034207966, 8.393221047155402, 8.402741693132036, 8.412110521914656, 8.42140090777686, 8.430697217432037, 8.440113783973313, 8.449864492755104, 8.460036984487749, 8.470838734400942, 8.48278433496105, 8.495991271245686, 8.510849572571898, 8.528593364418464, 8.549620525134262, 8.574812744552426, 8.606705378048085, 8.645766148056396, 8.69349707520585, 8.747922196371128, 8.812073167878056, 8.879617583362636, 8.963066593111842, 9.024947935237213, 9.069246583338101, 9.10467604170959, 9.134975519870077, 9.162360603541186, 9.18765412988997, 9.2113112738964, 9.233857816405868, 9.255365777321934\
]
pGasRS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
pGasRS[0] = [\
0.09631029816621017, 31.98194308658808, 54.00162714202444, 77.95770641876263, 105.26193194468239, 137.1509796826874, 174.9662829424174, 220.2760771829308, 274.9672972239619, 341.326884455086, 422.1453404143838, 520.8454601508513, 641.6336013645192, 789.6917111185263, 971.4124083139787, 1194.6835232028932, 1469.2391322788499, 1807.092587066414, 2223.0652771074733, 2735.4450852589807, 3366.797793065625, 4144.960100882646, 5104.248431477378, 6286.876764502952, 7744.723095669733, 9541.372767645464, 11754.021467762299, 14475.73618010661, 17816.953712913717, 21901.888972202367, 26857.714510382815, 32787.29695618313, 39701.59784678901, 47456.75408660215, 55550.66388684182, 62873.09621571801, 68301.84560081823, 71926.37699622661, 74504.03042938944, 76706.38047950226, 79109.43714898359, 82022.75634771032, 85940.6803254557, 91174.67909056113, 97868.79642667457, 166317.18093126826, 283663.87310855644, 407365.2395324743\
]
pGasRS[1] = [\
-2.3401800275133136, 3.4651714649905503, 3.989014178370019, 4.356166454231759, 4.656451833782303, 4.921082360505657, 5.164593286460005, 5.394881655914169, 5.616652171409531, 5.832840623554874, 6.0453496633058865, 6.255453376161025, 6.464017426385032, 6.671642630207505, 6.878751103470147, 7.085636595151019, 7.29249994868395, 7.499474527279836, 7.706642277953886, 7.914049438456456, 8.121717361838105, 8.32964844168052, 8.537828497718888, 8.746219686553115, 8.954766999554595, 9.163392650069907, 9.371950713592767, 9.580229159877234, 9.787905738763646, 9.994328166523356, 10.198308377491314, 10.397796431435653, 10.589146713895301, 10.767574135038192, 10.92505074615463, 11.048873628068366, 11.131692067167707, 11.183398333126673, 11.218608502627662, 11.247740171372675, 11.278587453200391, 11.314752004181319, 11.361412573581754, 11.420532495962007, 11.491383048670544, 12.021651972720548, 12.555545270807968, 12.91746545643577\
]
peRS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
peRS[0] = [\
8.75538650450228e-05, 0.0024227966794076366, 0.004016344736204967, 0.005839927426651347, 0.008020828310226385, 0.010669021512466069, 0.013905788912889626, 0.017873312082108374, 0.022748910796843436, 0.028753047966874033, 0.03615874376145408, 0.04530640530010186, 0.056614528659387035, 0.0705936083731309, 0.08786669804317858, 0.10920117836942063, 0.13553484529011106, 0.1680248601601973, 0.20812044890531226, 0.2576146480592527, 0.3187673814109147, 0.39443415996549563, 0.4882883971473001, 0.6052904959576122, 0.7516862775706549, 0.9361091282218668, 1.1718728294721346, 1.4762017348392757, 1.8760605385935594, 2.423949746271511, 3.20243804670365, 4.372237102165292, 6.318653026880507, 9.791088404885611, 17.310535842562892, 38.736889300551546, 115.150945735689, 329.2370750119993, 927.9182457545616, 1741.764108149898, 2604.575330650249, 3529.2749299629913, 4068.100525619303, 5145.267847506545, 6406.243087193756, 11960.28473311124, 22315.285038889197, 34988.55808485592\
]
peRS[1] = [\
-9.343256353490428, -6.022832753418254, -5.517383059588322, -5.143036909162479, -4.8257135818599295, -4.540410922422229, -4.275450056991238, -4.02444662383372, -3.7832380117931477, -3.549011501119005, -3.319836485171878, -3.0943068591355702, -2.8714896366170883, -2.650815671539782, -2.4319344079296377, -2.2145634248007937, -1.9985265109099277, -1.7836433333823842, -1.5696382856081406, -1.3562904227845551, -1.143293654079608, -0.9303030475157226, -0.7168490699267158, -0.5020467775829291, -0.28543622615936237, -0.06602321932000171, 0.15860317799114482, 0.38947239355924534, 0.6291741201025771, 0.8853983362559873, 1.1639124093100295, 1.4752748008120657, 1.8435060567854784, 2.2814726255299878, 2.851315324374102, 3.6567923579183232, 4.7462438393088595, 5.796778084004718, 6.83294363165817, 7.462653733863012, 7.865024920034494, 8.168847726552633, 8.310931468175644, 8.545832706681123, 8.765028276248042, 9.389346834337562, 10.013027150402772, 10.46277637516296\
]
pRadRS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
pRadRS[0] = [\
0.44368904474214005, 0.46512561889716125, 0.48918282664806584, 0.5147597751297295, 0.5414851438367154, 0.56912229204519, 0.597533434639085, 0.6265672855221673, 0.6562356933913268, 0.6866189187599715, 0.717806822755898, 0.749920590937172, 0.7830100616432191, 0.8170163954643335, 0.851811311882639, 0.8872975212415698, 0.9233567252795873, 0.9599485566661199, 0.9972108979368794, 1.0352907615260167, 1.0744875601806394, 1.1151948001916256, 1.158001141045864, 1.2040588201477214, 1.2540623558932842, 1.3094342402037438, 1.3735210722711768, 1.4480318847831117, 1.5367019344370259, 1.6497333788667508, 1.7944926381644706, 1.9847465171693297, 2.2548010452877447, 2.6361112526228276, 3.190662353084693, 3.966678180533641, 5.127062587346767, 6.717463057608163, 9.379313765969478, 12.013511438242972, 14.342491458680977, 16.526156951068526, 18.655524239418934, 20.815182384618144, 23.03135960106132, 25.31723335692404, 27.706623336709935, 30.19581497839805\
]
pRadRS[1] = [\
-0.812631311589179, -0.7654477617122879, -0.715018980756561, -0.6640549432016485, -0.6134396481220321, -0.563659943440527, -0.5149450391870829, -0.4674991113352007, -0.42123526586048854, -0.3759758440707941, -0.3315547952206046, -0.2877879568077688, -0.24460973295484223, -0.20209611643569048, -0.16039024160627946, -0.1195749287415353, -0.07973963455194877, -0.04087558276220449, -0.002792998855667861, 0.03468231627481089, 0.07184385972362861, 0.10902909834433672, 0.14669536450944065, 0.1856981996366045, 0.2263881665671832, 0.2695951662199576, 0.3173775684603868, 0.3702053135989303, 0.42963851890377924, 0.5006136862900448, 0.5847223291532373, 0.685491206825894, 0.8130617408085286, 0.9693048208417707, 1.1602285294395855, 1.377929014100701, 1.6345329001284128, 1.9047105620667324, 2.2385066010635555, 2.4860319695650404, 2.6632265619685924, 2.804944395454548, 2.9261423080964946, 3.035682642780934, 3.136856748176065, 3.2314853242017847, 3.3216714942396592, 3.407703337903925\
]
rhoRS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
rhoRS[0] = [\
3.999346457088632e-12, 1.2491496117439568e-10, 2.086287974326049e-10, 2.988537720068071e-10, 4.007969056960723e-10, 5.189121090427722e-10, 6.579504753785e-10, 8.234165016632847e-10, 1.0218197310294514e-09, 1.2609339070408233e-09, 1.5501309006380573e-09, 1.9007594433436662e-09, 2.3266554836745063e-09, 2.8447754653301685e-09, 3.4759169864478174e-09, 4.245500046814877e-09, 5.184655948625793e-09, 6.331365749387389e-09, 7.731725496705134e-09, 9.441932521013441e-09, 1.153010107849777e-08, 1.4078767497762437e-08, 1.7187337315551423e-08, 2.097329486806536e-08, 2.5579200552304178e-08, 3.117106126660785e-08, 3.792908680934367e-08, 4.606624821150738e-08, 5.579617165686008e-08, 6.724221183750073e-08, 8.042770632146529e-08, 9.5013259292964e-08, 1.0975696587711927e-07, 1.2282943152454362e-07, 1.3255714980273794e-07, 1.3945924129321457e-07, 1.4415118286215704e-07, 1.472125046985329e-07, 1.4476459917362395e-07, 1.427242828488914e-07, 1.4229059664053842e-07, 1.4307226614530057e-07, 1.4529300822601992e-07, 1.475100601129732e-07, 1.5101277433847043e-07, 2.490977753501782e-07, 4.1506754103089987e-07, 5.796083664361963e-07\
]
rhoRS[1] = [\
-26.2448901538854, -22.803387920747348, -22.290464531918776, -21.93106671899858, -21.637566286506875, -21.379286593841833, -21.14189145281803, -20.91755896591029, -20.70168074914836, -20.491413194469025, -20.284926457556573, -20.081012323612605, -19.878834015295414, -19.677781695037968, -19.477407511747945, -19.27740622746219, -19.077562352601372, -18.87774986586572, -18.677933778467338, -18.478105161531456, -18.278304736138583, -18.078598025718268, -17.879092926841427, -17.680015881434453, -17.481486294125997, -17.28377569605323, -17.087547557218432, -16.893185298008735, -16.701560578212803, -16.514964634278652, -16.335907114136123, -16.169249383580183, -16.02499731659874, -15.912469179554424, -15.836251965245603, -15.78549345548661, -15.752403207122812, -15.731388683862074, -15.748156867730247, -15.762351159814324, -15.765394415267105, -15.759915976677236, -15.744513387101117, -15.729369459336583, -15.705901405441702, -15.205420345468143, -14.694824580485923, -14.360913191759005\
]
kappa500RS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
kappa500RS[0] = [\
0.0005854197001629061, 0.0015258665671415077, 0.002075291042729248, 0.0026392851459552135, 0.0032540103106964684, 0.00394273509377969, 0.004726855818775361, 0.0056293144825227594, 0.006675723714571037, 0.007896958116130176, 0.009327795506910224, 0.011009500823621496, 0.012991029410229197, 0.01533101438645024, 0.018099855416295347, 0.02138158187481067, 0.025276592921755558, 0.029903987751685315, 0.03540402776615859, 0.04194323207331285, 0.04971833433416703, 0.05896296215687831, 0.06995468957884061, 0.08302272007776589, 0.09857071477036237, 0.11708832537638558, 0.13918650731711082, 0.16567381728185887, 0.19766521391569286, 0.23700154823935157, 0.28683753331700007, 0.3530092220543056, 0.44816683497842935, 0.5941091160960053, 0.871215336681592, 1.5824602898562259, 3.7019326470044, 8.283830814121886, 17.4270915735024, 26.56125718118278, 34.42335153827423, 41.8067368732007, 44.21234677776821, 51.87003395842858, 60.51895605428624, 9.555328651617602, 13.264295201640623, 18.76123237979555\
]
kappa500RS[1] = [\
-7.443181531790818, -6.4851927895618715, -6.177653873578944, -5.9372471765381745, -5.7278671015681635, -5.535880610269611, -5.354495029270375, -5.179767605785327, -5.009277658914445, -4.841277642250522, -4.67475657211535, -4.508996667729364, -4.343496205078471, -4.177877418264707, -4.011851328792242, -3.8452253875904177, -3.6778764924509995, -3.509763437856851, -3.340929686609669, -3.1714381922594206, -3.0013815138226168, -2.8308457922531716, -2.659907538247365, -2.488640972767671, -2.3169810719324566, -2.1448267112445696, -1.971940465973022, -1.797734379817943, -1.6211805181785532, -1.4396886052128517, -1.2488393095131753, -1.0412610975903542, -0.8025897163852149, -0.5206922793584222, -0.13786610343019137, 0.4589807814235486, 1.308855020307895, 2.1143055201139997, 2.8580259823558336, 3.279453657116902, 3.538735157869742, 3.7330574957596756, 3.7890040889393504, 3.9487412430465065, 4.102956639172672, 2.2570989728744046, 2.585075853998766, 2.9317926333072175\
]
kappaRosRS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
kappaRosRS[0] = [\
0.00018566454985234407, 0.0007208106991664422, 0.0010223773240871988, 0.0013552140246656428, 0.001740595256606241, 0.0021940403728050693, 0.0027314442538478507, 0.0033706973486863127, 0.004132971967013761, 0.005044930461058557, 0.006137205074115455, 0.00744690718446741, 0.009018079319931193, 0.010902955147244434, 0.013163815274090548, 0.015875406154937925, 0.019127013074192567, 0.023025645755574416, 0.02769991875541542, 0.03330332587889918, 0.04002013781329294, 0.048071563630207974, 0.05772465565860392, 0.069307259857458, 0.08321228672249117, 0.0999289404890866, 0.12010058084540065, 0.14451916422862787, 0.17428648377690167, 0.21120959091887184, 0.2581617986455252, 0.3204225859059123, 0.40930869624291444, 0.5435533316678947, 0.7934495443139774, 1.4234327602708523, 3.263878673558266, 7.130653637735977, 14.549421212761024, 21.67908732511645, 27.630510812373746, 33.07605871175489, 34.470618957610924, 39.84265028636776, 45.7565757843626, 4.385037900723823, 6.302653108267622, 8.74476833267795\
]
kappaRosRS[1] = [\
-8.591569007924434, -7.235134008319651, -6.885624653687904, -6.60379588534078, -6.353528122761235, -6.1220105158375695, -5.902924778959184, -5.692635627631029, -5.488758526196628, -5.289371409006238, -5.093385840113363, -4.8999564758108995, -4.708523903287707, -4.518721412065819, -4.330283480657467, -4.142984149967642, -3.9566536460275437, -3.7711466513893352, -3.5863257988106394, -3.40209801073982, -3.218372506221961, -3.0350644694129123, -2.8520708889632864, -2.6692056184253303, -2.486360265105123, -2.303295940695552, -2.1194257135598455, -1.934343155803921, -1.7470548752065245, -1.554904316633415, -1.3541687640891453, -1.1381145734325102, -0.8932856490861916, -0.6096274508910753, -0.23136532728313952, 0.3530713911239083, 1.182916265319781, 1.964402904521144, 2.6775512136346062, 3.0763480781353394, 3.3189206263639157, 3.4988097189144245, 3.5401073367821496, 3.6849379537560267, 3.823335514384466, 1.478198269053344, 1.8409706730443016, 2.16845561671634\
]
mmwRS = [ [ 0.0 for i in range(48) ] for j in range(2) ]
mmwRS = [\
2.0880302827501263e-24, 2.088053901239557e-24, 2.0880572054901676e-24, 2.0880568455178306e-24, 2.0880550118290014e-24, 2.0880525874564506e-24, 2.088049989927895e-24, 2.0880474518703448e-24, 2.0880450589752952e-24, 2.088042831636517e-24, 2.0880407663537612e-24, 2.0880388418977538e-24, 2.088037048686627e-24, 2.0880353950131364e-24, 2.088033896417814e-24, 2.0880325572993665e-24, 2.0880313844536366e-24, 2.088030371223066e-24, 2.0880294834315833e-24, 2.0880286906434414e-24, 2.0880279415396628e-24, 2.0880271737569225e-24, 2.088026297366018e-24, 2.088025136014319e-24, 2.0880235880297883e-24, 2.088021434200137e-24, 2.088018138588806e-24, 2.0880133776604157e-24, 2.0880063953581897e-24, 2.087995014939005e-24, 2.0879766515286554e-24, 2.087945748075252e-24, 2.0878876523397842e-24, 2.0877774313844097e-24, 2.087528773488479e-24, 2.086827979197091e-24, 2.0844694981624584e-24, 2.078433687760287e-24, 2.062613753101139e-24, 2.0428330321671528e-24, 2.023702734728706e-24, 2.0050738253429345e-24, 1.9970285215113487e-24, 1.9786993310308484e-24, 1.959601718197122e-24, 1.9469659043373885e-24, 1.93456515756968e-24, 1.920585462906523e-24\
]