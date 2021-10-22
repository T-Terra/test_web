require('dotenv').config()
const puppeteer = require('puppeteer');


async function Start() {
  //função para validação se o login foi efetuado
  async function messageError(page, browser, selector) {
    const msgError = await page.$(selector);
    if (msgError) {
      browser.close();
      throw ('Autenticação falhou');
    } else {
      browser.close();
      return ('Login efetuado com sucesso!');
    }
  }
  const browser = await puppeteer.launch({ headless: false });
  const page = await browser.newPage();
  // Pega a URL para navegar até a página
  await page.goto(process.env.DOMAIN);

  // clica no menu
  await page.click('[class="js-details-target btn-link d-lg-none mt-1"]');
  // Pega o botão de login
  await page.click('[href="/login"]');
  // Preenche o email e senha
  await page.type('[name="login"]', process.env.EMAIL,  {delay: 200});
  await page.type('[name="password"]', process.env.PASSWORD, {delay: 100});
  // Clica no botão de submit
  await page.click('[name="commit"]');
  // Aguarda a navegação chegar na página de login
  await page.waitForNavigation(process.env.DOMAIN_LOGIN);
  messageError(page, browser, '[class="container-lg px-2"]');
}

Start();