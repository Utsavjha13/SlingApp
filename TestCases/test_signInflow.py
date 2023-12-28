from PageObject.SignIn import signInApp
from Utilities.readProperties import login_read


class Test_signIn:
    email = login_read.getEmail()
    password = login_read.getPass()
    print(email,password)

    def test_login(self, dc):
        self.driver = dc
        self.driver.implicitly_wait(30)
        self.login = signInApp(dc)
        self.login.ClickProdEve()
        self.login.clickSignin()
        self.login.enterEmailPass(self.email, self.password)
        self.login.signInSubmit()
        title = self.login.profileTitle()
        if title == "Who's Watching?":
            assert True
        else:
            assert False
