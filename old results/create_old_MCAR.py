import numpy as np
import pickle

results = {
    5: {
        0.1:
            {'OrderBIMICE': {'RMSE': 4.58047792003467, 'MSE': 36.98904402349098, 'MAE': 1.0994796662900004, 'time': 303.514, 'MAPE': np.float64(0.0029760351869503794)}, 'FilterBIMICE': {'RMSE': 4.158742795190689, 'MSE': 31.429847820479974, 'MAE': 0.9921319822118583, 'time': 48.866, 'MAPE': np.float64(0.0010372062754659436)}, 'FullBIMICE': {'RMSE': 4.158743354602797, 'MSE': 31.429843358429935, 'MAE': 0.9921322543261779, 'time': 47.343999999999994, 'MAPE': np.float64(0.0010372066327755225)}, 'MICE': {'RMSE': 71.11394037160525, 'MSE': 7082.710358888031, 'MAE': 68.60779415301364, 'time': 1661.278, 'MAPE': np.float64(0.18570530748184144)}, 'SICE': {'RMSE': 65.29211426818063, 'MSE': 7556.775416023481, 'MAE': 60.814967160022974, 'time': 121965.469, 'MAPE': np.float64(0.16461194118502467)}, 'KNN': {'RMSE': 4.715192523768615, 'MSE': 39.76327059952222, 'MAE': 1.1066039762942408, 'time': 3583.008, 'MAPE': np.float64(0.002995319033578396)}},
        0.2: 
            {'OrderBIMICE': {'RMSE': 6.8623632707477675, 'MSE': 81.3067975615026, 'MAE': 2.251627240229702, 'time': 113.83600000000001, 'MAPE': np.float64(0.0030519043918776053)}, 'FilterBIMICE': {'RMSE': 6.305281496472473, 'MSE': 70.56645956841459, 'MAE': 2.0674100277525858, 'time': 28.128, 'MAPE': np.float64(0.0010865883246435036)}, 'FullBIMICE': {'RMSE': 6.305294935191171, 'MSE': 70.56652294785981, 'MAE': 2.0674269518718376, 'time': 54.858999999999995, 'MAPE': np.float64(0.0010865965782682467)}, 'MICE': {'RMSE': 54.940374997537724, 'MSE': 4356.376334242262, 'MAE': 51.79259618096293, 'time': 1911.8919999999998, 'MAPE': np.float64(0.07020080807660638)}, 'SICE': {'RMSE': 69.03644171598322, 'MSE': 7427.186694815227, 'MAE': 64.16696933926572, 'time': 944219.1020000001, 'MAPE': np.float64(0.0869733018152698)}, 'KNN': {'RMSE': 7.579651745350628, 'MSE': 97.30091263399315, 'MAE': 2.515014683119643, 'time': 6600.057, 'MAPE': np.float64(0.003408905443987466)}},
        0.3: 
            {'OrderBIMICE': {'RMSE': 8.45262559691661, 'MSE': 124.81660444283521, 'MAE': 3.357717671639813, 'time': 133.26399999999998, 'MAPE': np.float64(0.003034082233409471)}, 'FilterBIMICE': {'RMSE': 7.849939709982067, 'MSE': 109.90999793245312, 'MAE': 3.092274553150113, 'time': 36.041999999999994, 'MAPE': np.float64(0.0010712585661167414)}, 'FullBIMICE': {'RMSE': 7.849909760933084, 'MSE': 109.91009864093284, 'MAE': 3.0922710422231425, 'time': 36.935, 'MAPE': np.float64(0.0010712643631644759)}, 'MICE': {'RMSE': 80.13645357469082, 'MSE': 9782.186192697352, 'MAE': 77.17777632284405, 'time': 2679.32, 'MAPE': np.float64(0.06973895450859403)}, 'SICE': {'RMSE': 62.877672064396066, 'MSE': 6981.5329680075065, 'MAE': 57.28414600926187, 'time': 1403973.254, 'MAPE': np.float64(0.05176278253848956)}, 'KNN': {'RMSE': 9.185463223362792, 'MSE': 148.9881159875277, 'MAE': 3.7256156692146303, 'time': 8284.155, 'MAPE': np.float64(0.003366520183025268)}},
        0.4: 
            {'OrderBIMICE': {'RMSE': 9.623136670216645, 'MSE': 158.3099523492496, 'MAE': 4.474531307055335, 'time': 299.273, 'MAPE': np.float64(0.003072463703631502)}, 'FilterBIMICE': {'RMSE': 9.097621401586338, 'MSE': 142.70342867733686, 'MAE': 4.173733980374263, 'time': 34.451, 'MAPE': np.float64(0.001095118448107216)}, 'FullBIMICE': {'RMSE': 9.097574402222177, 'MSE': 142.6939568477828, 'MAE': 4.173724632796544, 'time': 46.266, 'MAPE': np.float64(0.0010951371718410793)}, 'MICE': {'RMSE': 59.0180428018302, 'MSE': 5283.606621084135, 'MAE': 56.0318760214546, 'time': 3367.372, 'MAPE': np.float64(0.03847462304059597)}, 'SICE': {'RMSE': 75.56292204301369, 'MSE': 9024.376737492054, 'MAE': 68.62065740488512, 'time': 2900399.1040000003, 'MAPE': np.float64(0.04711878512580806)}, 'KNN': {'RMSE': 10.291870611297362, 'MSE': 182.0033250686833, 'MAE': 4.922552639809471, 'time': 9035.953, 'MAPE': np.float64(0.0033801002333322034)}}
    },
    10: {
        0.1:
        {'OrderBIMICE': {'RMSE': 4.741643638052087, 'MSE': 38.62599963168586, 'MAE': 1.087277029642778, 'time': 266.256, 'MAPE': np.float64(0.0030389730642189435)}, 'FilterBIMICE': {'RMSE': 4.34823652544208, 'MSE': 33.64901907007606, 'MAE': 0.9857103414204433, 'time': 33.298, 'MAPE': np.float64(0.001068192927342774)}, 'FullBIMICE': {'RMSE': 4.348237102080887, 'MSE': 33.64903352791357, 'MAE': 0.9857106565633763, 'time': 32.966, 'MAPE': np.float64(0.0010681933833498025)}, 'MICE': {'RMSE': 61.61579323117241, 'MSE': 5090.579352059204, 'MAE': 58.86831981280633, 'time': 1064.857, 'MAPE': np.float64(0.1645387820854835)}, 'SICE': {'RMSE': 55.05121418544439, 'MSE': 5634.066565574016, 'MAE': 50.78809285995339, 'time': 254351.265, 'MAPE': np.float64(0.1419542968135343)}, 'KNN': {'RMSE': 4.849871675138482, 'MSE': 41.403614397251545, 'MAE': 1.0877986861789022, 'time': 3495.7400000000002, 'MAPE': np.float64(0.0030404311104379267)}},
        0.2:
        {'OrderBIMICE': {'RMSE': 6.64284399958298, 'MSE': 75.9374039931132, 'MAE': 2.2502230266517067, 'time': 175.60999999999999, 'MAPE': np.float64(0.003056445402937721)}, 'FilterBIMICE': {'RMSE': 6.185306430982153, 'MSE': 66.97963634775068, 'MAE': 2.067314395051774, 'time': 35.872, 'MAPE': np.float64(0.001081218896042948)}, 'FullBIMICE': {'RMSE': 6.185336838756513, 'MSE': 66.98006351588647, 'MAE': 2.0673271051744257, 'time': 47.190000000000005, 'MAPE': np.float64(0.0010812246175109085)}, 'MICE': {'RMSE': 67.0806279979996, 'MSE': 6108.613586821071, 'MAE': 64.27548045361151, 'time': 1784.029, 'MAPE': np.float64(0.0873044557927111)}, 'SICE': {'RMSE': 63.24152190860863, 'MSE': 6572.277124004967, 'MAE': 57.445600653772885, 'time': 1789619.374, 'MAPE': np.float64(0.07802752880832407)}, 'KNN': {'RMSE': 7.606257394774507, 'MSE': 102.91002980932383, 'MAE': 2.56670548157569, 'time': 6517.089999999999, 'MAPE': np.float64(0.003486318945695925)}},
        0.3:
        {'OrderBIMICE': {'RMSE': 8.473160900203577, 'MSE': 123.90783215202474, 'MAE': 3.395236440035415, 'time': 212.69, 'MAPE': np.float64(0.0030797347269017066)}, 'FilterBIMICE': {'RMSE': 7.8541473362037415, 'MSE': 107.95233067523792, 'MAE': 3.1014265900071982, 'time': 38.102999999999994, 'MAPE': np.float64(0.0010766416658937003)}, 'FullBIMICE': {'RMSE': 7.8537562603849835, 'MSE': 107.94456251605828, 'MAE': 3.101349905733989, 'time': 22.46, 'MAPE': np.float64(0.0010766191043568153)}, 'MICE': {'RMSE': 70.53962915663448, 'MSE': 7593.1620785185, 'MAE': 67.44423288842383, 'time': 2549.23, 'MAPE': np.float64(0.06117699012253723)}, 'SICE': {'RMSE': 71.51914192272827, 'MSE': 7850.992902932889, 'MAE': 66.3303308211508, 'time': 1371591.1739999999, 'MAPE': np.float64(0.06016659719717364)}, 'KNN': {'RMSE': 9.350793403082097, 'MSE': 148.29428758803112, 'MAE': 3.804027599949313, 'time': 8124.821000000001, 'MAPE': np.float64(0.00345053904450149)}},
        0.4:
        {'OrderBIMICE': {'RMSE': 9.545477183355917, 'MSE': 157.07942020980778, 'MAE': 4.470816037370389, 'time': 178.846, 'MAPE': np.float64(0.0030577813159308053)}, 'FilterBIMICE': {'RMSE': 9.018143642486542, 'MSE': 141.07471870871294, 'MAE': 4.189513140954014, 'time': 30.656, 'MAPE': np.float64(0.001097276626148561)}, 'FullBIMICE': {'RMSE': 9.02213734248156, 'MSE': 141.13647784752877, 'MAE': 4.191525789255645, 'time': 50.77, 'MAPE': np.float64(0.0010975683669608679)}, 'MICE': {'RMSE': 63.92459463419774, 'MSE': 5452.062615580812, 'MAE': 61.57272994190576, 'time': 3447.6200000000003, 'MAPE': np.float64(0.042112209854635756)}, 'SICE': {'RMSE': 68.28092246398033, 'MSE': 7531.177150034816, 'MAE': 63.014165077635525, 'time': 2901451.122, 'MAPE': np.float64(0.043098068675333966)}, 'KNN': {'RMSE': 10.340406431371783, 'MSE': 182.85278033576336, 'MAE': 4.85625851266637, 'time': 9054.428, 'MAPE': np.float64(0.003321401824910507)}}
    },
    15: {
        0.1:
            {'OrderBIMICE': {'RMSE': 4.9085770029412386, 'MSE': 41.512244052837495, 'MAE': 1.1277275236670663, 'time': 431.623, 'MAPE': np.float64(0.0030206987241082135)}, 'FilterBIMICE': {'RMSE': 4.616647435720877, 'MSE': 38.075330073236614, 'MAE': 1.045203022025382, 'time': 39.591, 'MAPE': np.float64(0.0010796697227133515)}, 'FullBIMICE': {'RMSE': 4.616649222789022, 'MSE': 38.07535628459063, 'MAE': 1.0452032450355115, 'time': 51.393, 'MAPE': np.float64(0.0010796698933420751)}, 'MICE': {'RMSE': 83.29968992869247, 'MSE': 9496.268362406045, 'MAE': 80.68098354073135, 'time': 1194.639, 'MAPE': np.float64(0.21610977734124462)}, 'SICE': {'RMSE': 76.81641119251802, 'MSE': 9215.73924362118, 'MAE': 72.68268712733423, 'time': 170215.125, 'MAPE': np.float64(0.19468576909107416)}, 'KNN': {'RMSE': 5.188065876167285, 'MSE': 47.789291226847816, 'MAE': 1.1875785507602883, 'time': 3677.4629999999997, 'MAPE': np.float64(0.003181013975250772)}},
        0.2:
            {'OrderBIMICE': {'RMSE': 7.231992189385886, 'MSE': 93.48310856585171, 'MAE': 2.2759607724549276, 'time': 187.661, 'MAPE': np.float64(0.0031149098163160503)}, 'FilterBIMICE': {'RMSE': 6.699813897678341, 'MSE': 81.91023842206823, 'MAE': 2.076161672362718, 'time': 29.145, 'MAPE': np.float64(0.0010974795198810763)}, 'FullBIMICE': {'RMSE': 6.69977318093973, 'MSE': 81.9087731827489, 'MAE': 2.0761506184295437, 'time': 47.737, 'MAPE': np.float64(0.0010974737994796724)}, 'MICE': {'RMSE': 49.38369028645663, 'MSE': 3140.49377034559, 'MAE': 47.051300695313564, 'time': 1933.1229999999998, 'MAPE': np.float64(0.06439502832387804)}, 'SICE': {'RMSE': 57.51684043978834, 'MSE': 5036.526743848183, 'MAE': 52.17369472441662, 'time': 838570.883, 'MAPE': np.float64(0.07140560409363585)}, 'KNN': {'RMSE': 8.564218305089442, 'MSE': 131.86909205953077, 'MAE': 2.745408533341742, 'time': 7013.326, 'MAPE': np.float64(0.0037574021897925293)}},
        0.3:
            {'OrderBIMICE': {'RMSE': 8.48059672489102, 'MSE': 123.78321404011545, 'MAE': 3.4108371582764834, 'time': 170.17499999999998, 'MAPE': np.float64(0.0031089259089009903)}, 'FilterBIMICE': {'RMSE': 7.903990326991841, 'MSE': 109.92415431707833, 'MAE': 3.1384927559296383, 'time': 28.942, 'MAPE': np.float64(0.0010986380248439267)}, 'FullBIMICE': {'RMSE': 7.904053793682705, 'MSE': 109.92542327551895, 'MAE': 3.1385694475094015, 'time': 40.815999999999995, 'MAPE': np.float64(0.001098649112603838)}, 'MICE': {'RMSE': 72.28177130097512, 'MSE': 8682.742096451671, 'MAE': 69.00414999531976, 'time': 2825.923, 'MAPE': np.float64(0.06289622746180656)}, 'SICE': {'RMSE': 70.0152853369351, 'MSE': 7774.521407730252, 'MAE': 62.539426132752254, 'time': 1381982.609, 'MAPE': np.float64(0.057003730524080386)}, 'KNN': {'RMSE': 9.176034862088734, 'MSE': 146.38350653831696, 'MAE': 3.7056502716589352, 'time': 8550.543, 'MAPE': np.float64(0.003377643553264169)}},
        0.4:
            {'OrderBIMICE': {'RMSE': 9.41924364766511, 'MSE': 154.1513561059611, 'MAE': 4.47916156100097, 'time': 183.164, 'MAPE': np.float64(0.003042678998340159)}, 'FilterBIMICE': {'RMSE': 8.926307533435809, 'MSE': 139.20504369373282, 'MAE': 4.191986033954801, 'time': 36.689, 'MAPE': np.float64(0.001087647488704937)}, 'FullBIMICE': {'RMSE': 8.927405418232441, 'MSE': 139.2210824188529, 'MAE': 4.192734489101914, 'time': 26.432000000000002, 'MAPE': np.float64(0.0010878047805294006)}, 'MICE': {'RMSE': 48.66453644860244, 'MSE': 3857.138510334927, 'MAE': 46.14099118140336, 'time': 3499.543, 'MAPE': np.float64(0.03134341615462527)}, 'SICE': {'RMSE': 71.0378053485025, 'MSE': 7367.985213232842, 'MAE': 64.87776264414781, 'time': 2929380.2369999997, 'MAPE': np.float64(0.04407124038020458)}, 'KNN': {'RMSE': 10.165287873517876, 'MSE': 177.52695800366024, 'MAE': 4.846649813477679, 'time': 9229.842, 'MAPE': np.float64(0.003292312500664132)}}
    }
}

with open("framingham__MCAR__results.pkl", "wb") as f:
        pickle.dump(results, f)