// Função para obter o nome do mês em português
function getNomeMes(mes) {
    const meses = [
        'Janeiro', 'Fevereiro', 'Março', 'Abril',
        'Maio', 'Junho', 'Julho', 'Agosto',
        'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ];
    return meses[mes];
}
// Função que preenche a data
function preencher_data(dia, mes, ano){
    const ano_formatado = String(ano).padStart(4, '0')
    const mes_formatado = String(mes + 1).padStart(2, '0')
    const dia_formatado = String(dia).padStart(2, '0')
    document.getElementById('id_date').value = `${ano_formatado}-${mes_formatado}-${dia_formatado}`
}
// Função principal para renderizar o calendário
function renderCalendario() {
    const dataAtual = new Date();
    const mesAtual = dataAtual.getMonth();
    const anoAtual = dataAtual.getFullYear();
    const diaAtual = dataAtual.getDate();
    // Atualiza o cabeçalho com mês e ano
    const headerElement = document.getElementById('mes-ano');
    headerElement.textContent = `${getNomeMes(mesAtual)} ${anoAtual}`;
    // Primeiro dia do mês e quantidade de dias no mês
    const primeiroDiaDoMes = new Date(anoAtual, mesAtual, 1).getDay();
    const ultimoDiaDoMes = new Date(anoAtual, mesAtual + 1, 0).getDate(); 
    const tbody = document.getElementById('dias-calendario');
    tbody.innerHTML = ''; 
    // Limpa conteúdo anterior
    let linha = document.createElement('tr');
    let diaContador = 1;
    // Adiciona células vazias antes do primeiro dia do mês
    for (let i = 0; i < primeiroDiaDoMes; i++) {
        const celulaVazia = document.createElement('td');
        linha.appendChild(celulaVazia);
    }
    // Renderiza os dias do mês
    while (diaContador <= ultimoDiaDoMes) {
        if (linha.children.length === 7) {
            tbody.appendChild(linha);
            linha = document.createElement('tr');
        } 
        const coluna = document.createElement('td');
        coluna.innerHTML = `<div class="dias" onclick="preencher_data(${diaContador}, ${mesAtual}, ${anoAtual})">${diaContador}</div>`;
        // Marca o dia atual
        if (diaContador === diaAtual && mesAtual === dataAtual.getMonth()) {
            coluna.classList.add('dia-atual');
        }
        if (diaContador < diaAtual && mesAtual === dataAtual.getMonth()) {
            coluna.classList.add('nao_clicavel')
        }
        // Marca fins de semana
        const diaSemana = new Date(anoAtual, mesAtual, diaContador).getDay();
        if (diaSemana === 0 || diaSemana === 6) {
            coluna.classList.add('fim-de-semana');
        } linha.appendChild(coluna);
        diaContador++;
    }
    // Adiciona a última linha se necessário
    if (linha.children.length > 0) {
        tbody.appendChild(linha);
    }
}
// Torna a função acessível para handlers inline como onclick
window.preencher_data = preencher_data;

// Renderiza o calendário quando a página carregar
document.addEventListener('DOMContentLoaded', renderCalendario);