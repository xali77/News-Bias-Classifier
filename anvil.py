from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def b22_click(self, **event_args):
    iris = anvil.server.call('cat',self.link.text)
    if iris:
      self.label_1.visible=True
      self.label_1.text="The article leans towards the - " + iris[0].capitalize()
      
      self.label_2.visible=True
      
      self.compound.visible=True
      self.compound.text="Compound = " + str(iris[1])
      
      self.negativity.visible=True
      self.negativity.text="Negativity = " + str(iris[2])
      
      self.positivity.visible=True
      self.positivity.text="Positivity = " + str(iris[3])
      
      self.neutrality.visible=True
      self.neutrality.text="Neutrality = " + str(iris[4])
      
      self.polarity.visible=True
      self.polarity.text="The Polarity(-2,2)  of the article was " + str(iris[5])
      
      self.subjectivity.visible=True
      self.subjectivity.text="The Subjectivity (0,2)  of the article was" + str(iris[6])
      
    pass





