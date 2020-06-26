### previous changes to arrays to fill in data using pseudo-symmetry

### saved changes for b2000aug31 ###
#arr[3269:,0:403] = np.fliplr(arr[3269:,403:806])
#arr[:200,7900:8659] = np.flipud(arr[200:400,7900:8659])
#arr[:,9058:] = np.fliplr(arr[:,8116:9058])
#arr[:730,6000:7900] = np.flipud(arr[730:1460,6000:7900])
#arr[:1200,4400:6000] = np.flipud(arr[1200:2400,4400:6000])
#arr[:2349,:1690] = np.flipud(arr[2349:2349*2,:1690])
#arr[:1884,1690:4400] = np.flipud(arr[1884:1884*2,1690:4400])
#arr[arr==0]=3

### saved changes for e2001sep08 ###
#arr[173:4000,:1168]=np.fliplr(arr[173:4000,1168:1168*2])
#arr[4000:8000,:680]=np.fliplr(arr[4000:8000,680:680*2])
#arr[:173,:] = np.flipud(arr[173:173*2,:])
#arr[7790:,:] = np.flipud(arr[5580:7790,:])

### saved changes for b2001sep03 ###
#arr[3516:4627,:500] = np.fliplr(arr[3516:4627,500:1000])
#arr[4657:5634,:205] = np.fliplr(arr[4657:5634,205:410])
#arr[8000:,:3290] = np.flipud(arr[6000:8000,:3290])
#arr[:1653,5217:8206] = np.flipud(arr[1653:2*1653,5217:8206])
#arr[1530:1780,8180:8484] = np.flipud(arr[1780:2030,8180:8484])
#arr[1530:1780,8484:8788]=np.fliplr(arr[1530:1780,8180:8484])
#arr[1530:1780,8788:9092]=np.fliplr(arr[1530:1780,8484:8788])
#arr[1530:1780,9092:9396]=np.fliplr(arr[1530:1780,8788:9092])
#arr[1530:1780,9396:9700]=np.fliplr(arr[1530:1780,9092:9396])
#arr[1530:1780,9700:]=np.fliplr(arr[1530:1780,9396:9696])
#arr[1780:2030,8180:]=np.flipud(arr[1530:1780,8180:])
#arr[2030:2616,8966:]=np.fliplr(arr[2030:2616,7932:8966])
#arr[:1535,8193:]=np.flipud(arr[1535:1535*2,8193:])
#arr[:3583,:1205]=np.fliplr(arr[:3583,1205:2410])
#arr[arr==0]=8

### saved changes for c2000aug07
#arr[8287:,364:5595] = np.flipud(arr[6574:8287,364:5595])
#arr[7590:,5595:9732] = np.flipud(arr[5180:7590,5595:9732])
#arr[:,9176:] = np.fliplr(arr[:,8352:9176])
#arr[6142:,8811:] = np.fliplr(arr[6142:,7622:8811])
#arr[5578:,:364] = np.fliplr(arr[5578:,364:2*364])
#arr[:1255,:2618] = np.flipud(arr[1255:1255*2,:2618])
#arr[:725,2618:6168] = np.flipud(arr[725:725*2,2618:6168])
#arr[arr == 0] = 4

### saved changes for e2000jul06
#arr[:20,:220] = 10
#arr[9614:,939:] = np.flipud(arr[9228:9614,939:])

### saved changes for e2000jul28
#arr[6588:,:] = np.flipud(arr[3176:6588,:])