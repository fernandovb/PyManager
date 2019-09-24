# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.lib.agw.ribbon as rb
import wx.grid

wx.ID_EXECUTE = 1000

###########################################################################
## Class TIRFAT
###########################################################################

class TIRFAT ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"IRFAT - Registro Fiscal - Entrada de Notas", pos = wx.DefaultPosition, size = wx.Size( 938,715 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		lay_tela = wx.BoxSizer( wx.VERTICAL )

		lay_ribbon = wx.BoxSizer( wx.VERTICAL )

		self.ribbon_entrada = rb.RibbonBar( self , wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_BAR_DEFAULT_STYLE )
		self.rb_page_dados = rb.RibbonPage( self.ribbon_entrada, wx.ID_ANY, u"Banco de dados" , wx.NullBitmap , 0 )
		self.rb_panel_entrada = rb.RibbonPanel( self.rb_page_dados, wx.ID_ANY, u"Fatura" , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb_entrada = rb.RibbonButtonBar( self.rb_panel_entrada, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb_entrada.AddSimpleButton( wx.ID_FIND, u"Localizar", wx.Bitmap( u"icons/ac_buscar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rbb_entrada.AddSimpleButton( wx.ID_NEW, u"Novo", wx.Bitmap( u"icons/ac_adicionar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rbb_entrada.AddSimpleButton( wx.ID_EDIT, u"Modificar", wx.Bitmap( u"icons/ac_editar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rbb_entrada.AddSimpleButton( wx.ID_DELETE, u"Excluir", wx.Bitmap( u"icons/ac_lixeira_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rb_panel_registro = rb.RibbonPanel( self.rb_page_dados, wx.ID_ANY, u"Registro" , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb_registro = rb.RibbonButtonBar( self.rb_panel_registro, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb_registro.AddSimpleButton( wx.ID_SAVE, u"Gravar", wx.Bitmap( u"icons/ac_confirmar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rbb_registro.AddSimpleButton( wx.ID_CANCEL, u"Cancelar", wx.Bitmap( u"icons/ac_cancelar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rb_panel_contabilidade = rb.RibbonPanel( self.rb_page_dados, wx.ID_ANY, u"Contabilidade" , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb_contabilidade = rb.RibbonButtonBar( self.rb_panel_contabilidade, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb_contabilidade.AddSimpleButton( wx.ID_EXECUTE, u"Contabilidade", wx.Bitmap( u"icons/ac_documento_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.ribbon_entrada.Realize()

		lay_ribbon.Add( self.ribbon_entrada, 1, wx.EXPAND, 5 )


		lay_tela.Add( lay_ribbon, 0, wx.EXPAND, 1 )

		lay_corpo = wx.BoxSizer( wx.VERTICAL )

		self.nb_entrada = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pn_entrada = wx.Panel( self.nb_entrada, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_principal = wx.BoxSizer( wx.HORIZONTAL )

		lay_ent_label_01 = wx.BoxSizer( wx.VERTICAL )

		self.lb_ent_documento = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Documento:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_documento.Wrap( -1 )

		lay_ent_label_01.Add( self.lb_ent_documento, 0, wx.ALL, 1 )

		self.lb_ent_dt_fatura = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Data da Fatura:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_dt_fatura.Wrap( -1 )

		lay_ent_label_01.Add( self.lb_ent_dt_fatura, 0, wx.ALL, 1 )

		self.lb_ent_dt_lancamento = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Data de Lançamento:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_dt_lancamento.Wrap( -1 )

		lay_ent_label_01.Add( self.lb_ent_dt_lancamento, 0, wx.ALL, 1 )

		self.lb_ent_montante = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Montante:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_montante.Wrap( -1 )

		lay_ent_label_01.Add( self.lb_ent_montante, 0, wx.ALL, 1 )


		lay_principal.Add( lay_ent_label_01, 0, wx.EXPAND, 1 )

		lay_ent_campos_01 = wx.BoxSizer( wx.VERTICAL )

		self.tc_ent_documento = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,26 ), 0 )
		self.tc_ent_documento.SetMaxLength( 10 )
		lay_ent_campos_01.Add( self.tc_ent_documento, 0, wx.ALL, 1 )

		lay_dt_fatura = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ent_dt_fatura = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,26 ), 0 )
		lay_dt_fatura.Add( self.tc_ent_dt_fatura, 0, wx.ALL, 1 )

		self.bt_ent_dt_fatura = wx.BitmapButton( self.pn_entrada, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ent_dt_fatura.SetBitmap( wx.Bitmap( u"icons/ac_calendario_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ent_dt_fatura.SetBitmapDisabled( wx.Bitmap( u"icons/ac_calendario_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_dt_fatura.Add( self.bt_ent_dt_fatura, 0, wx.ALL, 1 )


		lay_ent_campos_01.Add( lay_dt_fatura, 0, wx.EXPAND, 1 )

		lay_dt_lancamento = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ent_dt_lancamento = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,26 ), 0 )
		lay_dt_lancamento.Add( self.tc_ent_dt_lancamento, 0, wx.ALL, 1 )

		self.bt_ent_dt_lancamento = wx.BitmapButton( self.pn_entrada, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ent_dt_lancamento.SetBitmap( wx.Bitmap( u"icons/ac_calendario_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ent_dt_lancamento.SetBitmapDisabled( wx.Bitmap( u"icons/ac_calendario_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_dt_lancamento.Add( self.bt_ent_dt_lancamento, 0, wx.ALL, 1 )


		lay_ent_campos_01.Add( lay_dt_lancamento, 0, wx.EXPAND, 1 )

		lay_montante = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ent_montante = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size( 150,26 ), wx.TE_RIGHT )
		lay_montante.Add( self.tc_ent_montante, 0, wx.ALL, 1 )

		self.lb_ent_moeda = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Moeda:", wx.DefaultPosition, wx.Size( 60,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_moeda.Wrap( -1 )

		lay_montante.Add( self.lb_ent_moeda, 0, wx.ALL, 1 )

		self.tc_ent_moeda = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, u"BRL", wx.DefaultPosition, wx.Size( 40,26 ), 0 )
		self.tc_ent_moeda.SetMaxLength( 3 )
		lay_montante.Add( self.tc_ent_moeda, 0, wx.ALL, 1 )


		lay_ent_campos_01.Add( lay_montante, 0, wx.EXPAND, 5 )


		lay_principal.Add( lay_ent_campos_01, 1, wx.EXPAND, 1 )

		lay_ent_label_02 = wx.BoxSizer( wx.VERTICAL )

		self.lb_ent_operacao = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Operação:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_operacao.Wrap( -1 )

		lay_ent_label_02.Add( self.lb_ent_operacao, 0, wx.ALL, 1 )

		self.lb_ent_tp_documento = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Tipo documento:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_tp_documento.Wrap( -1 )

		lay_ent_label_02.Add( self.lb_ent_tp_documento, 0, wx.ALL, 1 )

		self.lb_ent_referencia = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Referência:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_referencia.Wrap( -1 )

		lay_ent_label_02.Add( self.lb_ent_referencia, 0, wx.ALL, 1 )

		self.lb_ent_pessoa = wx.StaticText( self.pn_entrada, wx.ID_ANY, u"Pessoa:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_pessoa.Wrap( -1 )

		lay_ent_label_02.Add( self.lb_ent_pessoa, 0, wx.ALL, 1 )


		lay_principal.Add( lay_ent_label_02, 0, wx.EXPAND, 1 )

		lay_ent_campos_02 = wx.BoxSizer( wx.VERTICAL )

		lay_ent_operacao = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ent_operacao = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		self.tc_ent_operacao.SetMaxLength( 3 )
		lay_ent_operacao.Add( self.tc_ent_operacao, 0, wx.ALL, 1 )

		self.bt_ent_operacao = wx.BitmapButton( self.pn_entrada, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ent_operacao.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ent_operacao.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_ent_operacao.Add( self.bt_ent_operacao, 0, wx.ALL, 1 )


		lay_ent_campos_02.Add( lay_ent_operacao, 1, wx.EXPAND, 1 )

		cb_ent_tp_documentoChoices = [ u"Fatura", u"Recibo", u"Nota de débito", wx.EmptyString, wx.EmptyString ]
		self.cb_ent_tp_documento = wx.ComboBox( self.pn_entrada, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,26 ), cb_ent_tp_documentoChoices, 0 )
		self.cb_ent_tp_documento.SetSelection( 0 )
		lay_ent_campos_02.Add( self.cb_ent_tp_documento, 0, wx.ALL, 1 )

		self.tc_ent_referencia = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,26 ), 0 )
		lay_ent_campos_02.Add( self.tc_ent_referencia, 0, wx.ALL, 1 )

		lay_pessoa = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ent_pessoa = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_ent_pessoa.SetMaxLength( 6 )
		lay_pessoa.Add( self.tc_ent_pessoa, 0, wx.ALL, 1 )

		self.bt_ent_pessoa = wx.BitmapButton( self.pn_entrada, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ent_pessoa.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ent_pessoa.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_pessoa.Add( self.bt_ent_pessoa, 0, wx.ALL, 1 )

		self.tc_ent_nome_pessoa = wx.TextCtrl( self.pn_entrada, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,26 ), 0 )
		self.tc_ent_nome_pessoa.Enable( False )

		lay_pessoa.Add( self.tc_ent_nome_pessoa, 0, wx.ALL, 1 )


		lay_ent_campos_02.Add( lay_pessoa, 0, wx.EXPAND, 1 )


		lay_principal.Add( lay_ent_campos_02, 1, wx.EXPAND, 5 )


		self.pn_entrada.SetSizer( lay_principal )
		self.pn_entrada.Layout()
		lay_principal.Fit( self.pn_entrada )
		self.nb_entrada.AddPage( self.pn_entrada, u"Principal", True )
		self.pn_pagamento = wx.Panel( self.nb_entrada, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_pagamento = wx.BoxSizer( wx.HORIZONTAL )

		lay_pag_label_01 = wx.BoxSizer( wx.VERTICAL )

		self.lb_ent_fpgto = wx.StaticText( self.pn_pagamento, wx.ID_ANY, u"Forma Pagamento:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_fpgto.Wrap( -1 )

		lay_pag_label_01.Add( self.lb_ent_fpgto, 0, wx.ALL, 1 )

		self.lb_ent_cpgto = wx.StaticText( self.pn_pagamento, wx.ID_ANY, u"Condição:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_cpgto.Wrap( -1 )

		lay_pag_label_01.Add( self.lb_ent_cpgto, 0, wx.ALL, 1 )

		self.lb_ent_vencimento = wx.StaticText( self.pn_pagamento, wx.ID_ANY, u"Vencimento:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_ent_vencimento.Wrap( -1 )

		lay_pag_label_01.Add( self.lb_ent_vencimento, 0, wx.ALL, 1 )


		lay_pagamento.Add( lay_pag_label_01, 0, wx.EXPAND, 1 )

		lay_pag_campos_01 = wx.BoxSizer( wx.VERTICAL )

		lay_form_pgto = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ent_form_pgto = wx.TextCtrl( self.pn_pagamento, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		self.tc_ent_form_pgto.SetMaxLength( 4 )
		lay_form_pgto.Add( self.tc_ent_form_pgto, 0, wx.ALL, 1 )

		self.bt_ent_form_pgto = wx.BitmapButton( self.pn_pagamento, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ent_form_pgto.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ent_form_pgto.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_form_pgto.Add( self.bt_ent_form_pgto, 0, wx.ALL, 1 )


		lay_pag_campos_01.Add( lay_form_pgto, 0, wx.EXPAND, 1 )

		lay_cond_pgto = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ent_condicao = wx.TextCtrl( self.pn_pagamento, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,26 ), 0 )
		self.tc_ent_condicao.SetMaxLength( 3 )
		lay_cond_pgto.Add( self.tc_ent_condicao, 0, wx.ALL, 1 )

		self.bt_ent_condicao = wx.BitmapButton( self.pn_pagamento, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ent_condicao.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ent_condicao.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_cond_pgto.Add( self.bt_ent_condicao, 0, wx.ALL, 1 )


		lay_pag_campos_01.Add( lay_cond_pgto, 0, wx.EXPAND, 1 )

		lay_vencimento = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ent_vencimento = wx.TextCtrl( self.pn_pagamento, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,26 ), 0 )
		lay_vencimento.Add( self.tc_ent_vencimento, 0, wx.ALL, 1 )

		self.bt_ent_vencimento = wx.BitmapButton( self.pn_pagamento, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ent_vencimento.SetBitmap( wx.Bitmap( u"icons/ac_calendario_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ent_vencimento.SetBitmapDisabled( wx.Bitmap( u"icons/ac_calendario_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_vencimento.Add( self.bt_ent_vencimento, 0, wx.ALL, 1 )


		lay_pag_campos_01.Add( lay_vencimento, 0, wx.EXPAND, 1 )


		lay_pagamento.Add( lay_pag_campos_01, 1, wx.EXPAND, 1 )


		self.pn_pagamento.SetSizer( lay_pagamento )
		self.pn_pagamento.Layout()
		lay_pagamento.Fit( self.pn_pagamento )
		self.nb_entrada.AddPage( self.pn_pagamento, u"Pagamento", False )

		lay_corpo.Add( self.nb_entrada, 0, wx.EXPAND |wx.ALL, 1 )

		lay_registro = wx.BoxSizer( wx.VERTICAL )

		lay_grid = wx.BoxSizer( wx.VERTICAL )

		lay_tabela = wx.BoxSizer( wx.VERTICAL )

		self.gd_ent_itens = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gd_ent_itens.CreateGrid( 0, 6 )
		self.gd_ent_itens.EnableEditing( True )
		self.gd_ent_itens.EnableGridLines( True )
		self.gd_ent_itens.EnableDragGridSize( False )
		self.gd_ent_itens.SetMargins( 0, 0 )

		# Columns
		self.gd_ent_itens.SetColSize( 0, 100 )
		self.gd_ent_itens.SetColSize( 1, 70 )
		self.gd_ent_itens.SetColSize( 2, 300 )
		self.gd_ent_itens.SetColSize( 3, 100 )
		self.gd_ent_itens.SetColSize( 4, 100 )
		self.gd_ent_itens.SetColSize( 5, 150 )
		self.gd_ent_itens.EnableDragColMove( False )
		self.gd_ent_itens.EnableDragColSize( True )
		self.gd_ent_itens.SetColLabelSize( 30 )
		self.gd_ent_itens.SetColLabelValue( 0, u"CÓDIGO" )
		self.gd_ent_itens.SetColLabelValue( 1, u"TIPO" )
		self.gd_ent_itens.SetColLabelValue( 2, u"DESCRIÇÃO" )
		self.gd_ent_itens.SetColLabelValue( 3, u"QTDE" )
		self.gd_ent_itens.SetColLabelValue( 4, u"V.UNIT." )
		self.gd_ent_itens.SetColLabelValue( 5, u"TOTAL" )
		self.gd_ent_itens.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gd_ent_itens.EnableDragRowSize( True )
		self.gd_ent_itens.SetRowLabelSize( 30 )
		self.gd_ent_itens.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gd_ent_itens.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		lay_tabela.Add( self.gd_ent_itens, 1, wx.EXPAND, 1 )


		lay_grid.Add( lay_tabela, 1, wx.EXPAND, 1 )

		lay_grid_botoes = wx.BoxSizer( wx.VERTICAL )

		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_item_consultar = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_consultar.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_consultar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.bt_item_consultar, 0, wx.ALL, 1 )

		self.bt_item_adicionar = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_adicionar.SetBitmap( wx.Bitmap( u"icons/ac_adicionar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_adicionar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_adicionar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.bt_item_adicionar, 0, wx.ALL, 1 )

		self.bt_item_editar = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_editar.SetBitmap( wx.Bitmap( u"icons/ac_editar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_editar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_editar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.bt_item_editar, 0, wx.ALL, 1 )

		self.bt_item_excluir = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_excluir.SetBitmap( wx.Bitmap( u"icons/ac_lixeira_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_excluir.SetBitmapDisabled( wx.Bitmap( u"icons/ac_lixeira_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.bt_item_excluir, 0, wx.ALL, 1 )


		bSizer6.Add( ( 5, 26), 0, 0, 1 )

		self.bt_item_confirmar = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_confirmar.SetBitmap( wx.Bitmap( u"icons/ac_confirmar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_confirmar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_confirmar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.bt_item_confirmar, 0, wx.ALL, 1 )

		self.bt_item_cancelar = wx.BitmapButton( self.m_panel6, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_cancelar.SetBitmap( wx.Bitmap( u"icons/ac_cancelar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_cancelar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_cancelar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		bSizer6.Add( self.bt_item_cancelar, 0, wx.ALL, 1 )


		self.m_panel6.SetSizer( bSizer6 )
		self.m_panel6.Layout()
		bSizer6.Fit( self.m_panel6 )
		lay_grid_botoes.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 0 )


		lay_grid.Add( lay_grid_botoes, 0, wx.EXPAND, 0 )


		lay_registro.Add( lay_grid, 0, wx.EXPAND, 1 )

		lay_detalhes = wx.BoxSizer( wx.VERTICAL )

		self.nb_detalhes = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pn_basico = wx.Panel( self.nb_detalhes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_basico = wx.BoxSizer( wx.HORIZONTAL )

		lay_bas_label_01 = wx.BoxSizer( wx.VERTICAL )

		self.lb_item_sequencia = wx.StaticText( self.pn_basico, wx.ID_ANY, u"Sequência:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_sequencia.Wrap( -1 )

		lay_bas_label_01.Add( self.lb_item_sequencia, 0, wx.ALL, 1 )

		self.lb_item_tipo = wx.StaticText( self.pn_basico, wx.ID_ANY, u"Tipo item:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_tipo.Wrap( -1 )

		lay_bas_label_01.Add( self.lb_item_tipo, 0, wx.ALL, 1 )

		self.lb_item_item = wx.StaticText( self.pn_basico, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_item.Wrap( -1 )

		lay_bas_label_01.Add( self.lb_item_item, 0, wx.ALL, 1 )

		self.lb_item_qtde = wx.StaticText( self.pn_basico, wx.ID_ANY, u"Quantidade:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_qtde.Wrap( -1 )

		lay_bas_label_01.Add( self.lb_item_qtde, 0, wx.ALL, 1 )

		self.lb_item_val_unitario = wx.StaticText( self.pn_basico, wx.ID_ANY, u"Valor unitário:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_val_unitario.Wrap( -1 )

		lay_bas_label_01.Add( self.lb_item_val_unitario, 0, wx.ALL, 1 )

		self.lb_item_montante = wx.StaticText( self.pn_basico, wx.ID_ANY, u"Montante:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_montante.Wrap( -1 )

		lay_bas_label_01.Add( self.lb_item_montante, 0, wx.ALL, 1 )


		lay_basico.Add( lay_bas_label_01, 0, wx.EXPAND, 1 )

		lay_bas_campos_01 = wx.BoxSizer( wx.VERTICAL )

		self.tc_item_sequencia = wx.TextCtrl( self.pn_basico, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,26 ), 0 )
		lay_bas_campos_01.Add( self.tc_item_sequencia, 0, wx.ALL, 1 )

		cb_item_tipoChoices = [ u"Material", u"Serviço" ]
		self.cb_item_tipo = wx.ComboBox( self.pn_basico, wx.ID_ANY, u"Material", wx.DefaultPosition, wx.Size( 90,26 ), cb_item_tipoChoices, 0 )
		self.cb_item_tipo.SetSelection( 0 )
		lay_bas_campos_01.Add( self.cb_item_tipo, 0, wx.ALL, 1 )

		lay_item = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_item = wx.TextCtrl( self.pn_basico, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_item_item.SetMaxLength( 6 )
		lay_item.Add( self.tc_item_item, 0, wx.ALL, 1 )

		self.bt_item_item = wx.BitmapButton( self.pn_basico, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_item.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_item.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_item.Add( self.bt_item_item, 0, wx.ALL, 1 )

		self.tc_item_descricao = wx.TextCtrl( self.pn_basico, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,26 ), 0 )
		self.tc_item_descricao.Enable( False )

		lay_item.Add( self.tc_item_descricao, 0, wx.ALL, 1 )


		lay_bas_campos_01.Add( lay_item, 0, wx.EXPAND, 1 )

		self.tc_item_qtde = wx.TextCtrl( self.pn_basico, wx.ID_ANY, u"0.000", wx.DefaultPosition, wx.Size( 100,26 ), wx.TE_RIGHT )
		lay_bas_campos_01.Add( self.tc_item_qtde, 0, wx.ALL, 1 )

		self.tc_item_val_unitario = wx.TextCtrl( self.pn_basico, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size( 100,26 ), wx.TE_RIGHT )
		lay_bas_campos_01.Add( self.tc_item_val_unitario, 0, wx.ALL, 1 )

		self.tc_item_montante = wx.TextCtrl( self.pn_basico, wx.ID_ANY, u"0.00", wx.DefaultPosition, wx.Size( 150,26 ), wx.TE_RIGHT )
		lay_bas_campos_01.Add( self.tc_item_montante, 0, wx.ALL, 1 )


		lay_basico.Add( lay_bas_campos_01, 1, wx.EXPAND, 1 )


		self.pn_basico.SetSizer( lay_basico )
		self.pn_basico.Layout()
		lay_basico.Fit( self.pn_basico )
		self.nb_detalhes.AddPage( self.pn_basico, u"Dados Básicos", True )
		self.pn_contabil = wx.Panel( self.nb_detalhes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_contabil = wx.BoxSizer( wx.HORIZONTAL )

		lay_con_rotulo_1 = wx.BoxSizer( wx.VERTICAL )

		self.lb_item_conta = wx.StaticText( self.pn_contabil, wx.ID_ANY, u"Conta contábil:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_conta.Wrap( -1 )

		lay_con_rotulo_1.Add( self.lb_item_conta, 0, wx.ALL, 1 )

		self.lb_item_centro_custo = wx.StaticText( self.pn_contabil, wx.ID_ANY, u"Centro de custo:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_centro_custo.Wrap( -1 )

		lay_con_rotulo_1.Add( self.lb_item_centro_custo, 0, wx.ALL, 1 )

		self.lb_item_centro_lucro = wx.StaticText( self.pn_contabil, wx.ID_ANY, u"Centro de lucro:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_centro_lucro.Wrap( -1 )

		lay_con_rotulo_1.Add( self.lb_item_centro_lucro, 0, wx.ALL, 1 )


		lay_contabil.Add( lay_con_rotulo_1, 0, wx.EXPAND, 1 )

		lay_con_campos_1 = wx.BoxSizer( wx.VERTICAL )

		lay_conta = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_conta = wx.TextCtrl( self.pn_contabil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_item_conta.SetMaxLength( 6 )
		lay_conta.Add( self.tc_item_conta, 0, wx.ALL, 1 )

		self.bt_item_conta = wx.BitmapButton( self.pn_contabil, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_conta.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_conta.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_conta.Add( self.bt_item_conta, 0, wx.ALL, 1 )


		lay_con_campos_1.Add( lay_conta, 0, wx.EXPAND, 1 )

		lay_centro_custo = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_centro_custo = wx.TextCtrl( self.pn_contabil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_item_centro_custo.SetMaxLength( 6 )
		lay_centro_custo.Add( self.tc_item_centro_custo, 0, wx.ALL, 1 )

		self.bt_item_centro_custo = wx.BitmapButton( self.pn_contabil, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_centro_custo.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_centro_custo.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_centro_custo.Add( self.bt_item_centro_custo, 0, wx.ALL, 1 )


		lay_con_campos_1.Add( lay_centro_custo, 0, wx.EXPAND, 1 )

		lay_centro_lucro = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_centro_lucro = wx.TextCtrl( self.pn_contabil, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_item_centro_lucro.SetMaxLength( 6 )
		lay_centro_lucro.Add( self.tc_item_centro_lucro, 0, wx.ALL, 1 )

		self.bt_item_centro_lucro = wx.BitmapButton( self.pn_contabil, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_centro_lucro.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_centro_lucro.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		lay_centro_lucro.Add( self.bt_item_centro_lucro, 0, wx.ALL, 1 )


		lay_con_campos_1.Add( lay_centro_lucro, 1, wx.EXPAND, 1 )


		lay_contabil.Add( lay_con_campos_1, 1, wx.EXPAND, 1 )


		self.pn_contabil.SetSizer( lay_contabil )
		self.pn_contabil.Layout()
		lay_contabil.Fit( self.pn_contabil )
		self.nb_detalhes.AddPage( self.pn_contabil, u"Contábil", False )

		lay_detalhes.Add( self.nb_detalhes, 1, wx.EXPAND |wx.ALL, 1 )


		lay_registro.Add( lay_detalhes, 1, wx.EXPAND, 1 )


		lay_corpo.Add( lay_registro, 1, wx.EXPAND, 1 )


		lay_tela.Add( lay_corpo, 1, wx.EXPAND, 1 )


		self.SetSizer( lay_tela )
		self.Layout()
		self.sb_entrada = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ent_consultar, id = wx.ID_FIND )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ent_adicionar, id = wx.ID_NEW )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ent_editar, id = wx.ID_EDIT )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ent_excluir, id = wx.ID_DELETE )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ent_confirmar, id = wx.ID_SAVE )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ent_cancelar, id = wx.ID_CANCEL )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ent_contabilidade, id = wx.ID_EXECUTE )
		self.bt_ent_dt_fatura.Bind( wx.EVT_BUTTON, self.ac_ent_dt_fatura )
		self.bt_ent_dt_lancamento.Bind( wx.EVT_BUTTON, self.ac_ent_dt_lancamento )
		self.bt_ent_operacao.Bind( wx.EVT_BUTTON, self.ac_ent_busca_operacao )
		self.bt_ent_pessoa.Bind( wx.EVT_BUTTON, self.ac_ent_busca_pessoa )
		self.bt_ent_form_pgto.Bind( wx.EVT_BUTTON, self.ac_ent_busca_fpgto )
		self.bt_ent_condicao.Bind( wx.EVT_BUTTON, self.ac_ent_busca_cpgto )
		self.bt_ent_vencimento.Bind( wx.EVT_BUTTON, self.ac_ent_dt_vencimento )
		self.bt_item_consultar.Bind( wx.EVT_BUTTON, self.ac_item_consultar )
		self.bt_item_adicionar.Bind( wx.EVT_BUTTON, self.ac_item_adicionar )
		self.bt_item_editar.Bind( wx.EVT_BUTTON, self.ac_item_editar )
		self.bt_item_excluir.Bind( wx.EVT_BUTTON, self.ac_item_excluir )
		self.bt_item_confirmar.Bind( wx.EVT_BUTTON, self.ac_item_confirmar )
		self.bt_item_cancelar.Bind( wx.EVT_BUTTON, self.ac_item_cancelar )
		self.bt_item_item.Bind( wx.EVT_BUTTON, self.ac_item_busca_item )
		self.tc_item_qtde.Bind( wx.EVT_KILL_FOCUS, self.on_focus_qtde )
		self.tc_item_qtde.Bind( wx.EVT_SET_FOCUS, self.off_focus_qtde )
		self.tc_item_val_unitario.Bind( wx.EVT_KILL_FOCUS, self.on_focus_val_unitario )
		self.tc_item_val_unitario.Bind( wx.EVT_SET_FOCUS, self.off_focus_val_unitario )
		self.bt_item_conta.Bind( wx.EVT_BUTTON, self.ac_item_busca_conta )
		self.bt_item_centro_custo.Bind( wx.EVT_BUTTON, self.ac_item_busca_ccusto )
		self.bt_item_centro_lucro.Bind( wx.EVT_BUTTON, self.ac_item_busca_clucro )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ac_ent_consultar( self, event ):
		event.Skip()

	def ac_ent_adicionar( self, event ):
		event.Skip()

	def ac_ent_editar( self, event ):
		event.Skip()

	def ac_ent_excluir( self, event ):
		event.Skip()

	def ac_ent_confirmar( self, event ):
		event.Skip()

	def ac_ent_cancelar( self, event ):
		event.Skip()

	def ac_ent_contabilidade( self, event ):
		event.Skip()

	def ac_ent_dt_fatura( self, event ):
		event.Skip()

	def ac_ent_dt_lancamento( self, event ):
		event.Skip()

	def ac_ent_busca_operacao( self, event ):
		event.Skip()

	def ac_ent_busca_pessoa( self, event ):
		event.Skip()

	def ac_ent_busca_fpgto( self, event ):
		event.Skip()

	def ac_ent_busca_cpgto( self, event ):
		event.Skip()

	def ac_ent_dt_vencimento( self, event ):
		event.Skip()

	def ac_item_consultar( self, event ):
		event.Skip()

	def ac_item_adicionar( self, event ):
		event.Skip()

	def ac_item_editar( self, event ):
		event.Skip()

	def ac_item_excluir( self, event ):
		event.Skip()

	def ac_item_confirmar( self, event ):
		event.Skip()

	def ac_item_cancelar( self, event ):
		event.Skip()

	def ac_item_busca_item( self, event ):
		event.Skip()

	def on_focus_qtde( self, event ):
		event.Skip()

	def off_focus_qtde( self, event ):
		event.Skip()

	def on_focus_val_unitario( self, event ):
		event.Skip()

	def off_focus_val_unitario( self, event ):
		event.Skip()

	def ac_item_busca_conta( self, event ):
		event.Skip()

	def ac_item_busca_ccusto( self, event ):
		event.Skip()

	def ac_item_busca_clucro( self, event ):
		event.Skip()


