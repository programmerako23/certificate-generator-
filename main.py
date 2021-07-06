from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.rl_config import defaultPageSize
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape

# make sure that your font is installed in your local machines 
pdfmetrics.registerFont(TTFont('Bold', 'Raleway-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Light', 'Raleway-Light.ttf'))
pdfmetrics.registerFont(TTFont('Extra', 'Raleway-Extrabold.ttf'))

fullName = "sdsdjs Mmmdzhomo"
# name of the file and the size
c= canvas.Canvas(f"certificate - {fullName}.pdf", pagesize=landscape(letter))

# draw the background
c.drawImage("files/cloud.png", 500,400, width=1.52*300,height=.87*300,mask=None) 
c.drawImage("files/image01.png", 260,40, width=1.52*200,height=.87*250,mask=None) 
c.drawImage("files/cloud.png", 500,-60, width=1.52*300,height=.87*300,mask=None)
c.drawImage("files/cloud.png", -225,100, width=1.52*300,height=.87*300,mask=None) 

# header 1
c.setFont('Bold',32)
c.setFillColor(HexColor(0x3f3d56))
c.drawCentredString(415,500, "Certificate of Completion")

# header 2
c.setFont('Light',24)
c.setFillColor(HexColor(0x3f3d56))
c.drawCentredString(415,450, "This is awarded to")

#Name
c.setFont('Extra',40)
c.setFillColor(HexColor(0x6c63ff))

c.drawCentredString(400,380, fullName)

# lower part of certicate
c.setFont('Light',18)
c.setFillColor(HexColor(0x3f3d56))
c.drawCentredString(415,350, "for participating in the ")
c.drawCentredString(415,330, "Contemporary Blues")
c.drawCentredString(415,310, "seminar held last March 14, 2020")
c.drawCentredString(415,290, "@ Angeles City ")

# file saving
c.showPage()
c.save()

