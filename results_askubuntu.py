results_askubuntu = {
    # SUPERVISED
    'supervised__nb': {
        'n': 40,
        'fracs': [1, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05],
        'class_acc_means': [0.9174311926605506, 0.9073394495412845, 0.8926605504587155, 0.8811926605504589, 0.7655963302752293, 0.6752293577981651, 0.5403669724770641, 0.41467889908256883, 0.328440366972477, 0.24596330275229356, 0.26605504587155965],
        'class_acc_stds': [1.1102230246251565e-16, 0.012612593655841747, 0.02230320326815268, 0.03982908946121101, 0.10009989959955046, 0.19347577631459964, 0.2055312073191207, 0.2304305189318772, 0.19375834025832708, 0.14895588124574727, 0.08078605490917916],
        'aug_acc_means': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        'aug_acc_stds': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'aug_frac_means': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        'p_means': [0.9616786511281925, 0.9536784576692833, 0.9436203041936986, 0.9370284779688449, 0.9167274450072617, 0.8569781548107237, 0.8017997298387207, 0.7768269162649897, 0.7506112054942331, 0.8398725664367868, 0.6665688073394495],
        'p_stds': [1.1102230246251565e-16, 0.011829146179160605, 0.01600075041860929, 0.025623359791865266, 0.02978589867822665, 0.16889520510241765, 0.2043000923342053, 0.2303664502663115, 0.24268861448750673, 0.21156152290909305, 0.19659294227098217],
        'r_means': [0.9174311926605506, 0.9073394495412845, 0.8926605504587155, 0.8811926605504589, 0.7655963302752293, 0.6752293577981651, 0.5403669724770641, 0.41467889908256883, 0.328440366972477, 0.24596330275229356, 0.26605504587155965],
        'r_stds': [1.1102230246251565e-16, 0.012612593655841747, 0.02230320326815268, 0.03982908946121101, 0.10009989959955046, 0.19347577631459964, 0.2055312073191207, 0.2304305189318772, 0.19375834025832708, 0.14895588124574727, 0.08078605490917916],
        'f1_means': [0.9386768106213171, 0.9277772052927068, 0.9136366637386143, 0.9019898135619882, 0.8029063038784905, 0.7163483650823731, 0.5866126104236258, 0.4621654036485139, 0.3998099263378728, 0.34305705195266534, 0.32628689910829967],
        'f1_stds': [1.1102230246251565e-16, 0.013442514855650836, 0.021348394184367833, 0.04037410029591157, 0.08242271835795772, 0.19445083259131238, 0.20531517726314388, 0.2546409761103574, 0.2170198993056594, 0.18526838058882955, 0.13278655013035112]
    },
    # KNN
    'knn_threshold__glove__cosine__nb': { # 20
        'fracs': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05],
        'class_acc_means': [0.9174311926605505, 0.9055045871559633, 0.8853211009174311, 0.7275229357798164, 0.6931192660550458, 0.5958715596330275, 0.4729357798165138, 0.26146788990825687, 0.27522935779816515, 0.268348623853211],
        'class_acc_stds': [0.005024977591790515, 0.02032891725335811, 0.035472687943451764, 0.16608038734100555, 0.11754134025725702, 0.223587505867544, 0.17943872971689792, 0.1785223037747337, 0.1783690100479228, 0.07592401368397454],
        'aug_acc_means': [0.9341666666666667, 0.9053968253968254, 0.9134052059052058, 0.7550063459931879, 0.7931261699257055, 0.64780990272123, 0.6607413417987775, 0.38265734889913783, 0, 0],
        'aug_acc_stds': [0.11790709619583263, 0.1045350929778856, 0.06849336714508246, 0.28615396365014933, 0.2521625742728934, 0.37090525285263093, 0.3017523480119609, 0.35752470170783446, 0, 0],
        'aug_frac_means': [0.7, 0.6954545454545455, 0.68125, 0.6818181818181819, 0.6518518518518518, 0.6046875, 0.49078947368421044, 0.45465116279069767, 0.29791666666666666, 0.2],
        'p_means': [0.9630667426424306, 0.9549317887047243, 0.9429675677038061, 0.9380722432786653, 0.9208180791437673, 0.8797022810440243, 0.8236523781821947, 0.7310816839371885, 0.9124159441475955, 0.61],
        'p_stds': [0.004773852463581721, 0.013744113847333782, 0.017213665621438917, 0.029348173784809275, 0.09715728233556097, 0.10795827100099431, 0.2051086106848807, 0.2277348565216652, 0.14124668196715534, 0.22516928233351535],
        'r_means': [0.9174311926605505, 0.9055045871559633, 0.8853211009174311, 0.7275229357798164, 0.6931192660550458, 0.5958715596330275, 0.4729357798165138, 0.26146788990825687, 0.27522935779816515, 0.268348623853211],
        'r_stds': [0.005024977591790515, 0.02032891725335811, 0.035472687943451764, 0.16608038734100555, 0.11754134025725702, 0.223587505867544, 0.17943872971689792, 0.1785223037747337, 0.1783690100479228, 0.07592401368397454],
        'f1_means': [0.9385079747614734, 0.9256840010753571, 0.9052303029159449, 0.7664642784317717, 0.7372963558673045, 0.6411306620625077, 0.5314672613406377, 0.31812035775544933, 0.3718406588051687, 0.3300251348792161],
        'f1_stds': [0.005226796399487922, 0.022154142840475555, 0.03744709871516307, 0.15432296007034485, 0.09883117809141378, 0.20842697648234015, 0.18421978920551257, 0.20313390516457233, 0.21151854718683105, 0.1291546973247805],
    },
    'knn_threshold__elmo__cosine__nb': { # 20
        'fracs': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05],
        'class_acc_means': [0.9178899082568807, 0.9114678899082568, 0.9004587155963304, 0.8325688073394495, 0.7775229357798165, 0.6302752293577981, 0.45366972477064216, 0.31605504587155964, 0.20366972477064219, 0.25688073394495403],
        'class_acc_stds': [0.012469979100062555, 0.014585424858334533, 0.026315246805988016, 0.1313201087497274, 0.12104791027844815, 0.18846680714609162, 0.16015613436518783, 0.18845285059102762, 0.14311926605504588, 0.08433383628830383],
        'aug_acc_means': [0.9400000000000001, 0.8899206349206349, 0.8904040404040405, 0.8311427461427462, 0.7187112247058068, 0.6154849652411571, 0.5239992806583196, 0.47891474968562264, 0, 0],
        'aug_acc_stds': [0.22000000000000003, 0.10831286509354271, 0.08460383650950665, 0.17415678952495253, 0.2731348368503598, 0.28383589398268466, 0.23930165712250817, 0.3360994474901988, 0, 0],
        'aug_frac_means': [0.5916666666666667, 0.6181818181818183, 0.60625, 0.5772727272727273, 0.5611111111111111, 0.5171875, 0.4855263157894737, 0.4069767441860465, 0.2552083333333333, 0.2],
        'p_means': [0.9633938278433691, 0.9579718796576596, 0.9512580755470663, 0.9024767713070467, 0.9210546780271551, 0.8941652758969273, 0.8900821587289478, 0.8596263756699537, 0.9552277195281782, 0.6619151376146788],
        'p_stds': [0.009663015670217375, 0.011378998120659779, 0.017279425986315756, 0.1441923786732066, 0.048036844388968464, 0.05130311814890544, 0.11142616644410237, 0.2189362596159664, 0.0828305297013575, 0.20336164704508525],
        'r_means': [0.9178899082568807, 0.9114678899082568, 0.9004587155963304, 0.8325688073394495, 0.7775229357798165, 0.6302752293577981, 0.45366972477064216, 0.31605504587155964, 0.20366972477064219, 0.25688073394495403],
        'r_stds': [0.012469979100062555, 0.014585424858334533, 0.026315246805988016, 0.1313201087497274, 0.12104791027844815, 0.18846680714609162, 0.16015613436518783, 0.18845285059102762, 0.14311926605504588, 0.08433383628830383],
        'f1_means': [0.9389118286284361, 0.9323831197699537, 0.9213319745016697, 0.8545239429061791, 0.8081871932092681, 0.6763216341007898, 0.5258937538399266, 0.39996321129758833, 0.30251631031955195, 0.32910037121094693],
        'f1_stds': [0.013325869541837712, 0.015673026198381537, 0.027141304488997164, 0.13824419013440847, 0.11681571666996413, 0.17758417336280416, 0.1747693817232909, 0.19884990484286827, 0.1936184695789862, 0.12923929381368623],
    },
    'knn_threshold__bert__cosine__nb': { 

    },
    'knn_threshold__infersent__cosine__nb': {
        'n': 40,
        'fracs': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05],
        'class_acc_means': [0.9146788990825689, 0.9073394495412845, 0.8903669724770642, 0.8697247706422019, 0.7821100917431193, 0.641743119266055, 0.5301834862385323, 0.37752293577981655, 0.2513761467889909, 0.2677981651376147],
        'class_acc_stds': [0.006551769200498035, 0.011926605504587151, 0.042685205463061635, 0.06006197175535013, 0.09507150481448831, 0.18160677332123887, 0.21672084250356868, 0.16501715790230634, 0.16934994564677242, 0.08716750285751343],
        'aug_acc_means': [0.9716666666666667, 0.8929563492063493, 0.9141566766566767, 0.9329913939259914, 0.8471460660923409, 0.7785798341422415, 0.661942779212993, 0.5164532759813585, 0, 0],
        'aug_acc_stds': [0.06772083217970012, 0.10539893761927756, 0.05445816877698465, 0.047180921730289475, 0.20195765610660923, 0.3053367646411059, 0.33575084669428085, 0.29857376406256736, 0, 0],
        'aug_frac_means': [0.7499999999999999, 0.6863636363636364, 0.746875, 0.7227272727272728, 0.6518518518518519, 0.603125, 0.6026315789473683, 0.4302325581395349, 0.32708333333333334, 0.1],
        'p_means': [0.9595067615251102, 0.9546808302656927, 0.9466005216578612, 0.9378061044460126, 0.9165639892589434, 0.9071908097481491, 0.8308167044956036, 0.826151918376689, 0.886098328896494,  0.669848623853211],
        'p_stds': [0.00647701912743283, 0.009542075454225366, 0.020427022244563758, 0.028938164735263755, 0.041232519260367625, 0.07539110591810169, 0.21126379044728746, 0.17892300354387775, 0.14242939754180634, 0.22918876895402632],
        'r_means': [0.9146788990825689, 0.9073394495412845, 0.8903669724770642, 0.8697247706422019, 0.7821100917431193, 0.641743119266055, 0.5301834862385323, 0.37752293577981655, 0.2513761467889909, 0.2677981651376147],
        'r_stds': [0.006551769200498035, 0.011926605504587151, 0.042685205463061635, 0.06006197175535013, 0.09507150481448831, 0.18160677332123887, 0.21672084250356868, 0.16501715790230634, 0.16934994564677242, 0.08716750285751343],
        'f1_means': [0.9358958613778807, 0.9283736234792901, 0.9112825102943811, 0.8901598355358008, 0.8173884261813813, 0.6939833572637311, 0.5876407839051657, 0.45127279897768136, 0.3528394629984114, 0.3394746416148843],
        'f1_stds': [0.0067962948815418036, 0.01186076719481661, 0.043483485086747674, 0.06120845202084751, 0.0750566664840973, 0.16352617200028616, 0.21960350704851836, 0.1932785482769348, 0.20153771758790653, 0.14334342656419083],
    },
    # LP 
    'lp_recursive__infersent__cosine__nb': { # w threshold = 0.9 & no class-norm
        'n': 40,
        'fracs': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05],
        'class_acc_means': [0.9158256880733944, 0.9084862385321101, 0.8860091743119266, 0.7832568807339448, 0.7486238532110092, 0.6522935779816514, 0.4158256880733945, 0.36651376146788994, 0.21628440366972476, 0.24220183486238533],
        'class_acc_stds': [0.009148472786779424, 0.014431326804348046, 0.03474676021359835, 0.1515662900885988, 0.1641766125377434, 0.19621877996763085, 0.19445849030702456, 0.24219097487468075, 0.15106845988632625, 0.10784792917321405],
        'aug_acc_means': [0.9200000000000002, 0.9710416666666667, 0.9725189393939395, 0.9651981351981351, 0.9943092105263158, 0.9917623604465711, 0.9576257321110262, 0.8834037297561326, 0.4757720247025773, 0.18120233857479207],
        'aug_acc_stds': [0.22626803181674213, 0.07117533856220457, 0.04795001359895411, 0.15675523775336395, 0.017166231174271542, 0.02234903224264066, 0.15751264409896543, 0.25786562967529897, 0.40405128994873923, 0.2578458599165338],
        'aug_frac_means': [0.5166666666666666, 0.509090909090909, 0.496875, 0.4329545454545455, 0.3916666666666666, 0.37890625, 0.2625, 0.3063953488372093, 0.26875, 0.3431372549019608],
        'p_means': [0.9614673330327002, 0.9562186412645127, 0.9426838404590697, 0.8774225602379273, 0.8653232432704911, 0.8328085993166269, 0.7276076217360622, 0.7193956197224546, 0.7428135584041546, 0.7319298820445609],
        'p_stds': [0.007982047831467512, 0.011332005128428215, 0.019724255053190594, 0.15168913344143334, 0.16870921448119727, 0.22902714571213376, 0.29489329572599443, 0.28214890550026245, 0.29678642279638523, 0.2500723151887341],
        'r_means': [0.9158256880733944, 0.9084862385321101, 0.8860091743119266, 0.7832568807339448, 0.7486238532110092, 0.6522935779816514, 0.4158256880733945, 0.36651376146788994, 0.21628440366972476, 0.24220183486238533],
        'r_stds': [0.009148472786779424, 0.014431326804348046, 0.03474676021359835, 0.1515662900885988, 0.1641766125377434, 0.19621877996763085, 0.19445849030702456, 0.24219097487468075, 0.15106845988632625, 0.10784792917321405],
        'f1_means': [0.9369264636463097, 0.9292945496956142, 0.9058812968911567, 0.8040189323496121, 0.7781049477010173, 0.6910541439716148, 0.48039692466380524, 0.428623723601929, 0.30094226729893075, 0.3272527450487391],
        'f1_stds': [0.00945783078809948, 0.014918019598538218, 0.03646051859267318, 0.156837373460423, 0.16575931001183294, 0.21132490738380288, 0.22381649596660994, 0.2612152348117555, 0.18866486453265718, 0.15681178440834298],
    }
}