class Credential:


  mycred = []

  def __init__(self, appType, appName, appUrl, appLogin, appPassword):
    self.appType = appType
    self.appName = appName
    self.appUrl = appUrl
    self.appLogin = appLogin
    self.appPassword

  #save
  @classmethod
  def saveCred(self):
    Credential.mycred.append(self)
  
  #display one or many
  @classmethod
  def displayCred(cls):
    return cls.mycred

    
  #search by app name4
  # delete selected
  # update data selected