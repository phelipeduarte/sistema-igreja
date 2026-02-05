/* Arquivo: static/js/mascaras.js */

window.addEventListener('load', function() {
    console.log("Script Blindado de CEP carregado!");

    // --- FUNÇÕES DE MÁSCARAS (Mantidas) ---
    function aplicarMascara(id, funcaoMascara, maxlength, placeholder) {
        var input = document.getElementById(id);
        if (input) {
            input.setAttribute("maxlength", maxlength);
            input.setAttribute("placeholder", placeholder);
            input.addEventListener("keyup", funcaoMascara);
        }
    }

    // 1. CPF
    aplicarMascara("id_cpf", function(e) {
        var v = e.target.value.replace(/\D/g, "");
        v = v.replace(/(\d{3})(\d)/, "$1.$2");
        v = v.replace(/(\d{3})(\d)/, "$1.$2");
        v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
        e.target.value = v;
    }, "14", "000.000.000-00");

    // 2. RG
    aplicarMascara("id_rg", function(e) {
        var v = e.target.value.replace(/[^0-9xX]/g, "");
        v = v.replace(/(\d{2})(\d)/, "$1.$2");
        v = v.replace(/(\d{3})(\d)/, "$1.$2");
        v = v.replace(/(\d{3})(\d{1,2})$/, "$1-$2");
        e.target.value = v;
    }, "13", "00.000.000-0");

    // 3. Telefone
    aplicarMascara("id_telefone", function(e) {
        var v = e.target.value.replace(/\D/g, "");
        v = v.replace(/^(\d{2})(\d)/g, "($1) $2");
        v = v.replace(/(\d)(\d{4})$/, "$1-$2");
        e.target.value = v;
    }, "15", "(00) 00000-0000");

    // --- 4. CEP COM PROTEÇÃO ---
    var cepInput = document.getElementById("id_cep");
    if (cepInput) {
        cepInput.setAttribute("maxlength", "9");
        cepInput.setAttribute("placeholder", "00000-000");

        // Máscara visual do CEP
        cepInput.addEventListener("keyup", function(e) {
            var v = e.target.value.replace(/\D/g, "");
            v = v.replace(/^(\d{5})(\d)/, "$1-$2");
            e.target.value = v;
        });

        // Busca ao sair do campo
        cepInput.addEventListener("blur", function(e) {
            var cep = e.target.value.replace(/\D/g, '');

            if (cep.length === 8) {
                // Tenta limpar os campos antes de buscar (só se eles existirem)
                preencherCampo("id_endereco", "...");
                preencherCampo("id_bairro", "...");
                preencherCampo("id_cidade", "...");

                var url = "https://viacep.com.br/ws/" + cep + "/json/";

                fetch(url)
                    .then(function(response) { return response.json(); })
                    .then(function(data) {
                        if (!data.erro) {
                            console.log("Sucesso:", data);
                            // Preenche APENAS se o campo existir na tela
                            preencherCampo("id_endereco", data.logradouro);
                            preencherCampo("id_bairro", data.bairro);
                            preencherCampo("id_cidade", data.localidade);
                            preencherCampo("id_uf", data.uf);
                            
                            // Tenta focar no número
                            var numeroInput = document.getElementById("id_numero");
                            if (numeroInput) numeroInput.focus();
                        } else {
                            alert("CEP não encontrado!");
                            limparEnderecos();
                        }
                    })
                    .catch(function(error) {
                        console.error("Erro Real:", error);
                        // Se der erro, não mostra alerta chato, apenas limpa e avisa no console
                        // alert("Erro de conexão com ViaCEP."); 
                        limparEnderecos();
                    });
            }
        });
    }

    // Função auxiliar para evitar erro se o campo não existir
    function preencherCampo(id, valor) {
        var campo = document.getElementById(id);
        if (campo) {
            campo.value = valor;
        }
    }

    function limparEnderecos() {
        preencherCampo("id_endereco", "");
        preencherCampo("id_bairro", "");
        preencherCampo("id_cidade", "");
        preencherCampo("id_uf", "");
    }
});