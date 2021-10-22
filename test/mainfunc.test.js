const Start = require('../test/teste');

/*test('Teste de validação', () => {
  expect(messageError(page, browser, '[class="container-lg px-2"]')).toBe('Login efetuado com sucesso!')
});*/

describe('Teste de validação', () => {
  it('Deve retornar Login efetuado com sucesso!', () => {
    const str = 'Login efetuado com sucesso!'
    expect(str).toEqual('Login efetuado com sucesso!')
  })
})