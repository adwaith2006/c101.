import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.A7eEaZti0AKyeTpSGz312VD85aDfT4iMzEgLXj-8Z5aXRaCyulLYdrie1tgesAu08TRhse4_QxCUEh2Sqc5pBtGuRYRVtU4cNgFzIXERg9Ub4bp88B8YRXE_Frss64YADmdWIdQ'
    transferData= TransferData(access_token)

    file_from=input("ENTER THE FILE PATH TO TRANSFER")
    file_to=input("ENTER THE FULL PATH TO UPLOAD TO DROPBOX")
    transferData.upload_file(file_from,file_to)
    print("FILE HAS BEEN MOVED SUCCESSFULLY")


main()
