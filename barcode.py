import cv2
import gspread
#from pyzbar.pyzbar import decode
import zxingcpp
import tkinter as tk

# ret, img = cam.read()
#         #cv2.imshow("img", img)
#         k = cv2.waitKey(1)
#         if k%256 == 27:
#            break
#         elif k%256 == 32:
#            barcode = zxingcpp.read_barcodes(img)
#            print(barcode)
#             later on I'll have the
           
def scanBarcode():
        ret, img = cam.read()
        cv2.imshow("img", img)
        barcode = zxingcpp.read_barcodes(img)
        print(barcode[0].text if len(barcode) > 0 else "none found") 
        #barcode = getBarcode.get()
        barcode = barcode[0].text if len(barcode) > 0 else "none found"
        try:
            row = memberSheet.col_values(1).index(barcode) + 1
        except ValueError:
            print("No info found")
            status.set(barcode + ":\nNo info found")
        else:
            member = memberSheet.row_values(row)
            print("Info found: " + member[2])
            status.set(barcode + ":\nInfo found: " + member[2])
            eventSheet.append_row(member)

if __name__ == "__main__":
    eventSheetN = input("Event Sheet Name:")

    gc = gspread.service_account() # This will connect to a set drive 
    memberSheet = gc.open("Members").get_worksheet(0)
    eventSheet = gc.open(eventSheetN).get_worksheet(0)

    cam = cv2.VideoCapture(0)
    cv2.namedWindow("img")
    #Tescv2.imshow("img", img)

    window = tk.Tk()
    captureImg = tk.Button(text="Scan", command=scanBarcode, justify="left") #fg="#7dc242")
    status = tk.StringVar(value="Waiting")
    statusLabel = tk.Label(textvariable=status,font=("Lucida Sans", 50), height=9, width=300, relief="raised", bg="#7dc242", fg="white")
    captureImg.pack()
    statusLabel.pack()

    getBarcode = tk.Entry(justify="left")
    getBarcode.pack()

    window.mainloop()



    # while True: # /shrug
    #     #ret, img = cam.read()
    #     #cv2.imshow("img", img)
    #     #k = cv2.waitKey(1)
    #     #if k%256 == 27:
    #     #    break
    #     #elif k%256 == 32:
    #     #    barcode = zxingcpp.read_barcodes(img)
    #     #    print(barcode)
    #         # later on I'll have the
    #     barcode = getBarcode.get()
    #     try:
    #         row = memberSheet.col_values(1).index(barcode) + 1
    #     except ValueError:
    #         print("No info found")
    #     else:
    #         member = memberSheet.row_values(row)
    #         print("Info found: " + member[1])
    #         eventSheet.append_row(member)
