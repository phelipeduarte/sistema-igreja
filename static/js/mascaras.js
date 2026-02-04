/* Arquivo: static/js/mascaras.js */

// Espera a página carregar completamente
window.addEventListener('load', function() {
    console.log("Script de máscaras CARREGADO com sucesso!"); // Teste no Console (F12)

    // --- FUNÇÃO PARA APLICAR MÁSCARA DE CPF ---
    var cpfInput = document.getElementById("id_cpf");
    if (cpfInput) {
        cpfInput.setAttribute("maxlength", "14");
        cpfInput.setAttribute("placeholder", "000.000.000-00"); // Ajuda visual
        
        cpfInput.addEventListener("keyup", function(e) {
            var v = e.target.value.replace(/\D/g, ""); // Remove tudo que não é dígito
            
            // Coloca ponto entre o terceiro e o quarto dígitos
            v = v.replace(/(\d{3})(\d)/, "$1.$2");
            
            // Coloca ponto entre o sexto e o sétimo dígitos
            v = v.replace(/(\d{3})(\d)/, "$1.$2");
            
            // Coloca ponto entre o nono e o décimo dígitos
            v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
            
            e.target.value = v;
        });
    }

    // --- FUNÇÃO PARA APLICAR MÁSCARA DE TELEFONE ---
    var telInput = document.getElementById("id_telefone");
    if (telInput) {
        telInput.setAttribute("maxlength", "15");
        telInput.setAttribute("placeholder", "(00) 00000-0000");

        telInput.addEventListener("keyup", function(e) {
            var v = e.target.value.replace(/\D/g, "");
            v = v.replace(/^(\d{2})(\d)/g, "($1) $2");
            v = v.replace(/(\d)(\d{4})$/, "$1-$2");
            e.target.value = v;
        });
    }
    
    // --- FUNÇÃO PARA APLICAR MÁSCARA DE CEP ---
    var cepInput = document.getElementById("id_cep");
    if (cepInput) {
        cepInput.setAttribute("maxlength", "9");
        cepInput.addEventListener("keyup", function(e) {
            var v = e.target.value.replace(/\D/g, "");
            v = v.replace(/^(\d{5})(\d)/, "$1-$2");
            e.target.value = v;
        });
    }
});