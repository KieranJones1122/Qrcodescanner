import qrcode

myqr = qrcode.make("https://github.com/KieranJones1122")
myqr1 = qrcode.make("https://www.linkedin.com/in/kieran-jones-944501274/")
myqr.save("myqr.png")
myqr1.save("myqr1.png")
