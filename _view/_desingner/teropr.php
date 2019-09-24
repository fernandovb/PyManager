<?php

/*
* PHP code generated with wxFormBuilder (version Oct 26 2018)
* http://www.wxformbuilder.org/
*
* PLEASE DO *NOT* EDIT THIS FILE!
*/

/*
 * Class TEROPR
 */

class TEROPR extends wxFrame {

	function __construct( $parent=null ){
		parent::__construct ( $parent, wxID_ANY, "EROPR - Cadastro de Operações", wxDefaultPosition, new wxSize( 700,500 ), wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		$this->SetSizeHints( wxDefaultSize, wxDefaultSize );

		$lay_tela = new wxBoxSizer( wxVERTICAL );

		$lay_ribbon = new wxBoxSizer( wxVERTICAL );

		/* WARNING: PHP code generation isn't supported for this widget yet. */
		$this->ribbon_operacao = new wxWindow( $this );
		/* WARNING: PHP code generation isn't supported for this widget yet. */
		$this->rb_page_dados = new wxWindow( $this );
		/* WARNING: PHP code generation isn't supported for this widget yet. */
		$this->rb_panel_entrada = new wxWindow( $this );
		/* WARNING: PHP code generation isn't supported for this widget yet. */
		$this->rbb_entrada = new wxWindow( $this );
		/* WARNING: PHP code generation isn't supported for this widget yet. */
		$this->rbt_consultar = new wxWindow( $this );
		/* WARNING: PHP code generation isn't supported for this widget yet. */
		$this->rbt_adicionar = new wxWindow( $this );
		/* WARNING: PHP code generation isn't supported for this widget yet. */
		$this->rbt_editar = new wxWindow( $this );
		/* WARNING: PHP code generation isn't supported for this widget yet. */
		$this->rbt_excluir = new wxWindow( $this );

		$lay_ribbon->Add( $this->ribbon_operacao, 1, wxEXPAND, 1 );


		$lay_tela->Add( $lay_ribbon, 0, wxEXPAND, 1 );

		$lay_corpo = new wxBoxSizer( wxVERTICAL );

		$this->pn_cabecalho = new wxPanel( $this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
		$lay_cabecalho = new wxBoxSizer( wxHORIZONTAL );

		$lay_cab_rotulos_1 = new wxBoxSizer( wxVERTICAL );

		$this->lb_operacao = new wxStaticText( $this->pn_cabecalho, wxID_ANY, "Operacão:", wxDefaultPosition, new wxSize( 150,26 ), wxALIGN_RIGHT );
		$this->lb_operacao->Wrap( -1 );

		$lay_cab_rotulos_1->Add( $this->lb_operacao, 0, wxALL, 1 );

		$this->lb_descricao = new wxStaticText( $this->pn_cabecalho, wxID_ANY, "Descrição:", wxDefaultPosition, new wxSize( 150,26 ), wxALIGN_RIGHT );
		$this->lb_descricao->Wrap( -1 );

		$lay_cab_rotulos_1->Add( $this->lb_descricao, 0, wxALL, 1 );


		$lay_cabecalho->Add( $lay_cab_rotulos_1, 0, wxEXPAND, 1 );

		$lay_cab_campos_1 = new wxBoxSizer( wxVERTICAL );

		$this->tc_operacao = new wxTextCtrl( $this->pn_cabecalho, wxID_ANY, wxEmptyString, wxDefaultPosition, new wxSize( 70,26 ), 0 );
		$lay_cab_campos_1->Add( $this->tc_operacao, 0, wxALL, 1 );

		$this->tc_descricao = new wxTextCtrl( $this->pn_cabecalho, wxID_ANY, wxEmptyString, wxDefaultPosition, new wxSize( 300,26 ), 0 );
		$lay_cab_campos_1->Add( $this->tc_descricao, 0, wxALL, 1 );


		$lay_cabecalho->Add( $lay_cab_campos_1, 1, wxEXPAND, 1 );


		$this->pn_cabecalho->SetSizer( $lay_cabecalho );
		$this->pn_cabecalho->Layout();
		$lay_cabecalho->Fit( $this->pn_cabecalho );
		$lay_corpo->Add( $this->pn_cabecalho, 0, wxEXPAND | wxALL, 1 );

		$this->nb_detalhes = new wxNotebook( $this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
		$this->pn_contabil = new wxPanel( $this->nb_detalhes, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
		$lay_contabil = new wxBoxSizer( wxHORIZONTAL );

		$lay_parte_1 = new wxStaticBoxSizer( new wxStaticBox( $this->pn_contabil, wxID_ANY, "Parte 1" ), wxVERTICAL );

		$lay_chave_lancamento = new wxBoxSizer( wxHORIZONTAL );

		$this->lb_con_chave_lancamento = new wxStaticText( $lay_parte_1->GetStaticBox(), wxID_ANY, "Chave de lançamento:", wxDefaultPosition, new wxSize( 150,26 ), wxALIGN_RIGHT );
		$this->lb_con_chave_lancamento->Wrap( -1 );

		$lay_chave_lancamento->Add( $this->lb_con_chave_lancamento, 0, wxALL, 1 );

		$this->tc_con_chave_lancamento = new wxTextCtrl( $lay_parte_1->GetStaticBox(), wxID_ANY, "XX", wxDefaultPosition, new wxSize( 35,26 ), 0 );
		$lay_chave_lancamento->Add( $this->tc_con_chave_lancamento, 0, wxALL, 1 );


		$lay_parte_1->Add( $lay_chave_lancamento, 0, wxEXPAND, 1 );

		$lay_con_conta = new wxBoxSizer( wxHORIZONTAL );

		$this->lb_con_conta = new wxStaticText( $lay_parte_1->GetStaticBox(), wxID_ANY, "Conta contábil:", wxDefaultPosition, new wxSize( 150,26 ), wxALIGN_RIGHT );
		$this->lb_con_conta->Wrap( -1 );

		$lay_con_conta->Add( $this->lb_con_conta, 0, wxALL, 1 );

		$this->tc_con_conta = new wxTextCtrl( $lay_parte_1->GetStaticBox(), wxID_ANY, wxEmptyString, wxDefaultPosition, new wxSize( 70,26 ), 0 );
		$lay_con_conta->Add( $this->tc_con_conta, 0, wxALL, 1 );

		$this->bt_con_conta = new wxBitmapButton( $lay_parte_1->GetStaticBox(), wxID_ANY, wxNullBitmap, wxDefaultPosition, wxDefaultSize, wxBU_AUTODRAW|0 );

		$this->bt_con_conta->SetBitmap( new wxBitmap( "icons/ac_buscar_16x16.png", wxBITMAP_TYPE_ANY ) );
		$this->bt_con_conta->SetBitmapDisabled( new wxBitmap( "icons/ac_buscar_16x16_inat.png", wxBITMAP_TYPE_ANY ) );
		$lay_con_conta->Add( $this->bt_con_conta, 0, wxALL, 1 );


		$lay_parte_1->Add( $lay_con_conta, 0, wxEXPAND, 1 );


		$lay_contabil->Add( $lay_parte_1, 1, wxEXPAND, 1 );


		$lay_contabil->Add( 5, 0, 0, wxEXPAND, 1, null );

		$lay_parte_2 = new wxStaticBoxSizer( new wxStaticBox( $this->pn_contabil, wxID_ANY, "Parte 2" ), wxVERTICAL );


		$lay_contabil->Add( $lay_parte_2, 1, wxEXPAND, 1 );


		$this->pn_contabil->SetSizer( $lay_contabil );
		$this->pn_contabil->Layout();
		$lay_contabil->Fit( $this->pn_contabil );
		$this->nb_detalhes->AddPage( $this->pn_contabil, "Contábil", true );
		$this->pn_fiscal = new wxPanel( $this->nb_detalhes, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
		$bSizer8 = new wxBoxSizer( wxVERTICAL );


		$this->pn_fiscal->SetSizer( $bSizer8 );
		$this->pn_fiscal->Layout();
		$bSizer8->Fit( $this->pn_fiscal );
		$this->nb_detalhes->AddPage( $this->pn_fiscal, "Fiscal", false );
		$this->pn_estoque = new wxPanel( $this->nb_detalhes, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
		$lay_estoque = new wxBoxSizer( wxHORIZONTAL );

		$lay_est_rotulo_1 = new wxBoxSizer( wxVERTICAL );

		$this->lb_est_ativo = new wxStaticText( $this->pn_estoque, wxID_ANY, "Conta estoque:", wxDefaultPosition, new wxSize( 150,26 ), 0 );
		$this->lb_est_ativo->Wrap( -1 );

		$lay_est_rotulo_1->Add( $this->lb_est_ativo, 0, wxALL, 1 );

		$this->lb_est_conta = new wxStaticText( $this->pn_estoque, wxID_ANY, "Conta contábil:", wxDefaultPosition, new wxSize( 150,26 ), 0 );
		$this->lb_est_conta->Wrap( -1 );

		$lay_est_rotulo_1->Add( $this->lb_est_conta, 0, wxALL, 1 );


		$lay_estoque->Add( $lay_est_rotulo_1, 0, wxEXPAND, 1 );

		$lay_est_campos_1 = new wxBoxSizer( wxVERTICAL );

		$this->ck_est_ativo = new wxCheckBox( $this->pn_estoque, wxID_ANY, "Utilizar estoque", wxDefaultPosition, new wxSize( 150,26 ), 0 );
		$lay_est_campos_1->Add( $this->ck_est_ativo, 0, wxALL, 1 );

		$lay_est_conta = new wxBoxSizer( wxHORIZONTAL );

		$this->tc_est_conta = new wxTextCtrl( $this->pn_estoque, wxID_ANY, wxEmptyString, wxDefaultPosition, new wxSize( 70,26 ), 0 );
		$this->tc_est_conta->SetMaxLength( 6 );
		$lay_est_conta->Add( $this->tc_est_conta, 0, wxALL, 1 );

		$this->bt_est_conta = new wxBitmapButton( $this->pn_estoque, wxID_ANY, wxNullBitmap, wxDefaultPosition, wxDefaultSize, wxBU_AUTODRAW|0 );

		$this->bt_est_conta->SetBitmap( new wxBitmap( "icons/ac_buscar_16x16.png", wxBITMAP_TYPE_ANY ) );
		$this->bt_est_conta->SetBitmapDisabled( new wxBitmap( "icons/ac_buscar_16x16_inat.png", wxBITMAP_TYPE_ANY ) );
		$lay_est_conta->Add( $this->bt_est_conta, 0, wxALL, 1 );


		$lay_est_campos_1->Add( $lay_est_conta, 0, wxEXPAND, 1 );


		$lay_estoque->Add( $lay_est_campos_1, 1, wxEXPAND, 1 );


		$this->pn_estoque->SetSizer( $lay_estoque );
		$this->pn_estoque->Layout();
		$lay_estoque->Fit( $this->pn_estoque );
		$this->nb_detalhes->AddPage( $this->pn_estoque, "Estoque", false );

		$lay_corpo->Add( $this->nb_detalhes, 1, wxEXPAND | wxALL, 1 );


		$lay_tela->Add( $lay_corpo, 1, wxEXPAND, 1 );


		$this->SetSizer( $lay_tela );
		$this->Layout();
		$this->sb_operacao = $this->CreateStatusBar( 1, wxSTB_SIZEGRIP, wxID_ANY );

		// Connect Events
		// event wxEVT_COMMAND_RIBBONBUTTON_CLICKED isn't currently supported by wxPHP
		// event wxEVT_COMMAND_RIBBONBUTTON_CLICKED isn't currently supported by wxPHP
		// event wxEVT_COMMAND_RIBBONBUTTON_CLICKED isn't currently supported by wxPHP
		// event wxEVT_COMMAND_RIBBONBUTTON_CLICKED isn't currently supported by wxPHP
		$this->ck_est_ativo->Connect( wxEVT_COMMAND_CHECKBOX_CLICKED, array($this, "ac_est_utilizar") );
		$this->bt_est_conta->Connect( wxEVT_COMMAND_BUTTON_CLICKED, array($this, "ac_est_busca_conta") );
	}


	function __destruct( ){
	}


	// Virtual event handlers, overide them in your derived class
	function ac_cab_consultar( $event ){
		$event->Skip();
	}

	function ac_cab_adicionar( $event ){
		$event->Skip();
	}

	function ac_cab_editar( $event ){
		$event->Skip();
	}

	function ac_cab_excluir( $event ){
		$event->Skip();
	}

	function ac_est_utilizar( $event ){
		$event->Skip();
	}

	function ac_est_busca_conta( $event ){
		$event->Skip();
	}

}

?>
