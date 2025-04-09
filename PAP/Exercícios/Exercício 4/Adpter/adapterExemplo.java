 interface processadorPag {
    void processoPagamento(double valorPagamento);
}

 class pagamentoAdapter implements processadorPag {
    private antigoSistemaPagamento antigoSistemaPag;
    public pagamentoAdapter(antigoSistemaPagamento antigoSistemaPag){
        this.antigoSistemaPag = antigoSistemaPag;
    }
    public void processoPagamento(double valorPagamento){
        antigoSistemaPag.pagar("BRL", valorPagamento);
    }
}

 class antigoSistemaPagamento {
    void pagar (String carencia, double valorPagamento){
        System.out.println("Pagamento realizado: " + valorPagamento + " " + carencia);
    }    
}

 class adapterExemplo {
    public static void main(String[] args) {
        antigoSistemaPagamento antigoSistema = new antigoSistemaPagamento();
        processadorPag processadorPagamento = new pagamentoAdapter(antigoSistema);

        processadorPagamento.processoPagamento(150.00);
    }
}
