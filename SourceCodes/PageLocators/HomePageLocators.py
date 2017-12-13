class HomePageLocators:

    def __init__(self):
        pass

    _signInLink = "cssselector:a[href*='signin.ebay.com']"
    _regLink = "cssselector:a[href*='reg.ebay.com']"

    _sellLink = "cssselector:div#gh-top a[href*='sell']"

    _userNameGreetingLink = "cssselector:button#gh-ug.gh-ua.gh-control"
    _signOutLink = "cssselector:ul#gh-uu > li#gh-uo"
