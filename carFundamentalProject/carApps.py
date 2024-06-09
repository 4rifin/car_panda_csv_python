import pandas as pd
path ='/Users/arifin/PycharmProject/carFundamentalProject/.venv/dataFile/DATA_CAR.csv'
data = pd.read_csv(path, usecols=['id', 'model','factory','Year'])
resultDataDictionary = data.to_dict(orient='records')
dataByCarModel = None
success = None

# converting column data to list
dataFrame = pd.DataFrame(resultDataDictionary)
print(dataFrame)
while True:
  try:
    inputSearchModelName = input("Please Input Search Car Model :").strip().lower()
    print('Search Data.....')
    for data in resultDataDictionary:
      if(data['model'].strip().lower() == inputSearchModelName):
        dataByCarModel = data
        success = True
      else:
        success = False

      if(dataByCarModel != None):
        if(inputSearchModelName == dataByCarModel['model'].strip().lower()):
          success = True
          message = "Product Car available :" + inputSearchModelName +"\nData :"+ str(dataByCarModel)
        else:
          success = False
          message = "Product Car Not Available: " + inputSearchModelName
      else:
          success = False
          message = "Product Car Not available: " + inputSearchModelName

    print(f'=======Result========= \n{message}')

    if success:
      print('======================')
      print(f'Please press button\nEdit[2]\nDelete[3]\nExit[4]')
      nextInput = input("Please Input :").strip().lower()
      if (nextInput == '3'):
        print('=======Result Data Delete=========')
        deleteDataName = dataByCarModel['model']
        deleteDataId = dataByCarModel['id']-1
        del resultDataDictionary[deleteDataId]
        print(f'Delete data {deleteDataName} berhasil')
        print(f'Data Delete :{dataByCarModel}')
        print('======================')
        dataFrames = pd.DataFrame(resultDataDictionary)
        print(dataFrames)
      elif(nextInput == '2'):
        print('======= Data Edit=========')
        editDataId = dataByCarModel['id']-1
        editDataCarModel = dataByCarModel['model']
        editDataEmail = dataByCarModel['factory']
        editDataAddress = dataByCarModel['Year']
        print(f'Data : {dataByCarModel}')
        print(f'Edit data {editDataCarModel}\nPlease press button \nEdit Model[1] \nEdit Factory[2]\nEdit Year[3]')
        print('=======================')
        nextInputEdit = input("Please pilih data menu yang akan di edit :").strip().lower()
        if(nextInputEdit == '1'):
          nextInputEditCarModel = input("Input Ubah model name :").strip().lower()
          resultDataDictionary[editDataId]['model'] = nextInputEditCarModel
          print('===Result Data Edit (Model)=====')
          print(f'Data :{resultDataDictionary[editDataId]}')
          dataFrames = pd.DataFrame(resultDataDictionary)
          print(dataFrames)
          print('=======================')
        elif(nextInputEdit == '2'):
          nextInputEditFactory = input("Input Ubah Factory Name :").strip().lower()
          resultDataDictionary[editDataId]['factory'] = nextInputEditFactory
          print('Edit Data.....')
          print('===Result Data Edit (Factory)=====')
          print(f'Data :{resultDataDictionary[editDataId]}')
          dataFrames = pd.DataFrame(resultDataDictionary)
          print(dataFrames)
          print('=======================')
        elif(nextInputEdit == '3'):
          nextInputEditYear = input("Input Ubah Year :").strip().lower()
          resultDataDictionary[editDataId]['Year'] = nextInputEditYear
          print('Edit Data.....')
          print('===Result Data Edit (Year)=====')
          print(f'Data :{resultDataDictionary[editDataId]}')
          dataFrames = pd.DataFrame(resultDataDictionary)
          print(dataFrames)
          print('=======================')
        else:
          print(f'Data : {nextInputEdit}')

      elif(nextInput == '4'):
        print('=================')
        print(f'Exit...')
        print(f'Thank you :) ')
        dataFrames = pd.DataFrame(resultDataDictionary)
        print(dataFrames)

      break
    else:
      retry = input("Apakah Anda Ingin Melanjutkan Pencarian ? (yes/no): ").strip().lower()

    if retry == 'yes':
      continue
    elif retry == 'no':
      break
    else:
      while True:
        retryAgain = input("Apakah Anda Ingin Melanjutkan Pencarian ? (yes/no): ").strip().lower()
        if retryAgain == 'yes':
          countinueSearch = True
          break
        elif retryAgain == 'no':
          countinueSearch = False
          break

      if countinueSearch == False:
        break

  except:
    break
