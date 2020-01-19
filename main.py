from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.rl_config import defaultPageSize
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape


pdfmetrics.registerFont(TTFont('Bold', 'Raleway-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Light', 'Raleway-Light.ttf'))
pdfmetrics.registerFont(TTFont('Extra', 'Raleway-Extrabold.ttf'))
c= canvas.Canvas("certificate_sample_out.pdf", pagesize=landscape(letter))
# cloud en
c.drawImage("cloud.png", 500,400, width=1.52*300,height=.87*300,mask=None) 
# cloud es
 
# cloud wm


c.drawImage("image01.png", 260,40, width=1.52*200,height=.87*250,mask=None) 
c.drawImage("cloud.png", 500,-60, width=1.52*300,height=.87*300,mask=None)
c.drawImage("cloud.png", -225,100, width=1.52*300,height=.87*300,mask=None) 
# this is for certi
c.setFont('Bold',32)
c.setFillColor(HexColor(0x3f3d56))
c.drawCentredString(415,500, "Certificate of Completion")

# This is for "This is awarded to "
c.setFont('Light',24)
c.setFillColor(HexColor(0x3f3d56))
c.drawCentredString(415,450, "This is awarded to")


#This is for name 
c.setFont('Extra',40)
c.setFillColor(HexColor(0x6c63ff))

# this where you can put your name 
c.drawCentredString(400,380, "Adjbhay Mmmdzhomo")
'''
for participating in the 
"Contemporary Blues" 
seminar held last March 14, 2020
@ Angeles City 
'''
c.setFont('Light',18)
c.setFillColor(HexColor(0x3f3d56))
c.drawCentredString(415,350, "for participating in the ")
c.drawCentredString(415,330, "Contemporary Blues")
c.drawCentredString(415,310, "seminar held last March 14, 2020")
c.drawCentredString(415,290, "@ Angeles City ")

c.showPage()
c.save()

