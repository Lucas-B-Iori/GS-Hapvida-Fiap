const inputNome = document.getElementById('inputNome')
const inputEmail = document.getElementById('inputEmail')
const botaoEnviar = document.getElementById('enviar')
const botaoLimpar = document.getElementById('limpar')

const secao = document.getElementById('form')

function validaCampo(valor) {
    return valor.trim().length > 3
}

function limpaCampos() {
    inputNome.value = ''
    inputEmail.value = ''
}

function validaEmail(campo) {
    if(!campo.value.includes('@') || !campo.value.includes('.com')) {
        return false
    }
    const [ dominio, email ] = campo.value.split('@')
    if (!validaCampo(dominio) || !validaCampo(email)) {
        return false
    }
    return true
}

function limpaMensagem(mensagem, classe) {
    mensagem.classList.remove(classe)
    mensagem.textContent = ''
}

function submeteFormulario(msg, classe) {
    const mensagem = document.createElement('div')
    mensagem.textContent = msg
    mensagem.classList.add(classe)
    secao.appendChild(mensagem)
    setTimeout(() => limpaMensagem(mensagem, classe), 3000)
}

function validaFormulario(e) {
    e.preventDefault()
    if (!validaCampo(inputNome.value)) {
        submeteFormulario('O nome deve ter pelo menos 3 letras', 'erro')
        return false
    }
    if (!validaEmail(inputEmail)) {
        submeteFormulario('O email deve ter o dominio, @ e .com', 'erro')
        return false
    }
    submeteFormulario('Formulário submetido com sucesso, obrigado', 'certo')
    limpaCampos()
    return true
}

botaoEnviar.addEventListener('click', validaFormulario)

botaoLimpar.addEventListener('click', limpaCampos)