
import EigenPortfolio as ep
import oracle as oc
import math
import numpy as np
from utils import plotAndEval as pe
from utils import readin, yfReader, dataUtil as du
import bestStock as bs


#Re_ep, D, M= ep.main()

# get return from senarios other than baseline
#Re_oa = oa.main()
# note here the form of date is [('2014-11-05', 10), ('2014-11-12', 15), ('2014-11-19', 20), ...],
# different from what pe.plotEval() expects, but should still work
dateSelected, stockPrice = du.getData() 
c = [0.001]*10
c_0 = 0.001
startingFund = 10000
Time = range(len(stockPrice)/3,len(stockPrice))
print stockPrice

'''
Re_oa = oa.solveOracle(stockPrice, startingFund,c, c_0)
Re_bs = bs.bestStock(stockPrice)
print len(Re_oa), len(Re_bs), len(dateSelected)
pe = pe.plotEval(dateSelected[:-1], 2014)
pe.addReturn(Re_oa, 'Oracle')
pe.addReturn(Re_bs, 'BestStock')
pe.generatePlot()
'''

'''

# an example of how to call oracle
Re_oa = oa.solveOracle([stockPrice[i], for i in Time], startingFund, c, c_0)


Re_ep = ep.baseline(stockPrice, Time)


Re_rnn_test = [0.98699791543185711, 1.0302469525486231, 0.98419808596372604, 0.99246294936165214, 0.99644162878394127, 1.0021397278178483, 0.96342739462852478, 1.0093504190444946, 1.0058030257932842, 1.0108546251431108, 0.99463294167071581, 0.97932521626353264, 0.97577562183141708, 1.0199341848492622, 0.97513593733310699, 1.0044565079733729, 1.0034554465673864, 1.0128548936918378, 0.99346175231039524, 1.0034837136045098, 0.99961665680166334, 1.0050968392752111, 1.0159019455313683, 0.99151359498500824, 0.99023677315562963, 0.99652773281559348, 0.99470548797398806, 0.99392154207453132, 0.98556465562433004, 0.98763161618262529, 1.023836724460125, 0.99858165776822716, 0.98902222979813814, 1.0086559215560555, 0.99305670382454991, 0.99331719195470214, 0.93084041774272919, 0.99285905668511987, 0.99414464179426432, 1.0204637832939625, 0.9648950919508934, 1.0024581379257143, 1.0318303816020489, 0.99603453790768981, 1.01806422136724, 1.0426683016121387, 1.0002083564177155, 0.98638583719730377, 1.0043056388385594, 1.0001035495661199, 1.0008589714998379, 0.98385184444487095, 1.0227256827056408, 0.9882742203772068, 0.99722882523201406, 0.96293649077415466, 0.95701735094189644, 0.96920986101031303, 1.0095726065337658, 1.0137687837705016, 0.98237369954586029, 1.0280960500240326, 0.9960013129748404, 1.0202718172222376, 1.0036219651810825, 1.012405363842845, 1.0129508962854743, 1.0043390495702624, 0.99198687169700861, 1.0136306099593639, 1.0205097328871489, 0.99291858077049255, 0.97202472202479839, 0.9990381557145156, 1.005024541169405, 1.0365979261696339, 1.0000580915948376, 1.0061451056972146, 0.97116700932383537, 1.0086263455450535, 0.98388566635549068, 1.0077547738328576, 1.0345463305711746, 1.0153770381584764, 0.9934319956228137, 0.98830546531826258, 1.0173863414674997, 1.0052987327799201, 1.0018104179762304, 1.0060948939062655, 1.0010422504274175, 0.97746757976710796, 1.0167436208575964, 0.99684423580765724, 0.99761039111763239, 0.99156889878213406, 0.99836198694538325, 0.99289787374436855, 0.98267624899744987, 1.034266397356987, 1.016364136710763, 1.0138454157859087, 1.00006840727292, 1.0236411299556494, 0.99788738670758903, 0.99796734610572457, 0.98912438470870256, 1.0059455977752805, 1.0026211210060865, 0.99575534649193287, 1.0204333234578371, 0.98114312067627907, 1.0065573779866099, 1.0207186471670866, 1.0130014345049858, 1.0165528748184443, 0.98727479483932257, 0.99914521537721157, 0.97479545138776302, 0.99783506477251649, 0.99797992967069149, 0.99124008230865002, 0.99878159444779158, 1.0191203597933054, 0.99518317542970181, 0.99573235400021076, 0.97727182134985924, 1.0202201921492815, 0.99497101083397865, 1.0058765853755176, 1.0104942256584764, 0.99677972076460719, 1.0028020553290844, 1.0008093026699498, 0.9906464759260416, 1.0022914225701243, 1.0002781198127195, 1.0118468115106225, 0.99728987435810268, 0.99822638870682567, 0.98634239565581083, 1.002572680125013, 0.99498100997880101, 1.0158645864576101, 1.0139346187934279, 0.99905628542182967, 1.0132189206779003, 1.0016863415949047, 1.0069735208526254]
Re_rnn_test = np.array(Re_rnn_test)
Re_rnn_test -= 1
#Re_cnn = cnn.main()
Re_cnn_test = [-0.014807714149355888, -0.05512503162026405, -0.04122151806950569, -0.012694030068814754, 0.0571012943983078, 0.013195204548537731, -0.10323681682348251, 0.05336137115955353, 0.019293472170829773, 0.011776459403336048, 0.005290846340358257, 0.012009579688310623, 0.01347731426358223, 0.026381151750683784, -0.028121378272771835, -0.0044950200244784355, 0.0018804875435307622, 0.0626310482621193, -0.025363033637404442, 0.1563202142715454, 0.06463785469532013, -0.027876459062099457, -0.008470351807773113, -0.07526734471321106, 0.041258327662944794, 0.010079851374030113, 0.04389847442507744, -0.007912030443549156, 0.0163759533315897, 0.027143102139234543, -0.012412595562636852, 0.02627021074295044, 0.017093472182750702, 0.05476566031575203, 0.0022737307008355856, 0.016268141567707062, -0.019795579835772514, 0.015223965048789978, -0.0006209193961694837, -0.009678196161985397, 0.018862446770071983, -0.01187615841627121, 0.020047029480338097, 0.004612908698618412, -0.009518500417470932, -0.010059393011033535, 0.05487605929374695, 0.03095647692680359, 0.009577382355928421, 0.0014921074034646153, 0.0016580418450757861, 0.03231893479824066, 0.011774206534028053, -0.06993858516216278, -0.012055364437401295, -0.006034148391336203, -0.03401101753115654, 0.06029924005270004, 0.1588975340127945, 0.024834275245666504, -0.029615264385938644, -0.06051868572831154, -0.023021016269922256, 0.004709329921752214, 0.006495135370641947, 0.0328625813126564, 0.048296380788087845, 0.010540599934756756, -0.027613693848252296, 0.002334429882466793, 0.0741630271077156, 0.022138116881251335]
Date_cnn_test = [('2016-05-25', '2016-06-01'), ('2016-06-01', '2016-06-08'), ('2016-06-08', '2016-06-15'), ('2016-06-15', '2016-06-22'), ('2016-06-22', '2016-06-29'), ('2016-06-29', '2016-07-06'), ('2016-07-06', '2016-07-13'), ('2016-07-13', '2016-07-20'), ('2016-07-20', '2016-07-27'), ('2016-07-27', '2016-08-03'), ('2016-08-03', '2016-08-10'), ('2016-08-10', '2016-08-17'), ('2016-08-17', '2016-08-24'), ('2016-08-24', '2016-08-31'), ('2016-08-31', '2016-09-07'), ('2016-09-07', '2016-09-14'), ('2016-09-14', '2016-09-21'), ('2016-09-21', '2016-09-28'), ('2016-09-28', '2016-10-05'), ('2016-10-05', '2016-10-12'), ('2016-10-12', '2016-10-19'), ('2016-10-19', '2016-10-26'), ('2016-10-26', '2016-11-02'), ('2016-11-02', '2016-11-09'), ('2016-11-09', '2016-11-16'), ('2016-11-16', '2016-11-23'), ('2016-11-23', '2016-11-30'), ('2016-11-30', '2016-12-07'), ('2016-12-07', '2016-12-14'), ('2016-12-14', '2016-12-21'), ('2016-12-21', '2016-12-28'), ('2016-12-28', '2017-01-04'), ('2017-01-04', '2017-01-11'), ('2017-01-11', '2017-01-18'), ('2017-01-18', '2017-01-25'), ('2017-01-25', '2017-02-01'), ('2017-02-01', '2017-02-08'), ('2017-02-08', '2017-02-15'), ('2017-02-15', '2017-02-22'), ('2017-02-22', '2017-03-01'), ('2017-03-01', '2017-03-08'), ('2017-03-08', '2017-03-15'), ('2017-03-15', '2017-03-22'), ('2017-03-22', '2017-03-29'), ('2017-03-29', '2017-04-05'), ('2017-04-05', '2017-04-12'), ('2017-04-12', '2017-04-19'), ('2017-04-19', '2017-04-26'), ('2017-04-26', '2017-05-03'), ('2017-05-03', '2017-05-10'), ('2017-05-10', '2017-05-17'), ('2017-05-17', '2017-05-24'), ('2017-05-24', '2017-05-31'), ('2017-05-31', '2017-06-07'), ('2017-06-07', '2017-06-14'), ('2017-06-14', '2017-06-21'), ('2017-06-21', '2017-06-28'), ('2017-06-28', '2017-07-05'), ('2017-07-05', '2017-07-12'), ('2017-07-12', '2017-07-19'), ('2017-07-19', '2017-07-26'), ('2017-07-26', '2017-08-02'), ('2017-08-02', '2017-08-09'), ('2017-08-09', '2017-08-16'), ('2017-08-16', '2017-08-23'), ('2017-08-23', '2017-08-30'), ('2017-08-30', '2017-09-06'), ('2017-09-06', '2017-09-13'), ('2017-09-13', '2017-09-20'), ('2017-09-20', '2017-09-27'), ('2017-09-27', '2017-10-04'), ('2017-10-04', '2017-10-11')]

# adjust off-set:
# Baseline omits the last day in both cnn and oracle
Re_oa = Re_oa[:-1]
# Re_cnn_test should be shortest
Re_ep = Re_ep[len(Re_ep)-len(Re_cnn_test):]
Re_oa = Re_oa[len(Re_oa)-len(Re_cnn_test):]
Re_rnn_test = Re_rnn_test[len(Re_rnn_test)-len(Re_cnn_test):]


pe = pe.plotEval(Date_cnn_test, 2016)
pe.addReturn(Re_ep, 'Baseline')
pe.addReturn(Re_oa, 'Oracle')
pe.addReturn(Re_cnn_test, 'CNN')
pe.addReturn(Re_rnn_test,'RNN')
pe.generatePlot()
pe.eval()
'''
