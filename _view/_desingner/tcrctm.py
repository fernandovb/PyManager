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
## Class TCRCTM
###########################################################################

class TCRCTM ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Contratos", pos = wx.DefaultPosition, size = wx.Size( 1082,742 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		lay_tela = wx.BoxSizer( wx.VERTICAL )

		lay_ribbon = wx.BoxSizer( wx.VERTICAL )

		self.ribbon_contrato = rb.RibbonBar( self , wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_BAR_DEFAULT_STYLE )
		self.rb_page_dados = rb.RibbonPage( self.ribbon_contrato, wx.ID_ANY, u"Banco de Dados" , wx.NullBitmap , 0 )
		self.rb_panel_dados = rb.RibbonPanel( self.rb_page_dados, wx.ID_ANY, u"Contrato" , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb_contrato = rb.RibbonButtonBar( self.rb_panel_dados, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb_contrato.AddSimpleButton( wx.ID_FIND, u"Localizar", wx.Bitmap( u"icons/ac_buscar_32x32.png", wx.BITMAP_TYPE_ANY ), u"Localizar contrato")
		self.rbb_contrato.AddSimpleButton( wx.ID_NEW, u"Novo", wx.Bitmap( u"icons/ac_adicionar_32x32.png", wx.BITMAP_TYPE_ANY ), u"Novo contrato")
		self.rbb_contrato.AddSimpleButton( wx.ID_EDIT, u"Modificar", wx.Bitmap( u"icons/ac_editar_32x32.png", wx.BITMAP_TYPE_ANY ), u"Altera informações do contrato")
		self.rbb_contrato.AddSimpleButton( wx.ID_DELETE, u"Excluir", wx.Bitmap( u"icons/ac_lixeira_32x32.png", wx.BITMAP_TYPE_ANY ), u"Inativa contrato")
		self.rb_panel_registro = rb.RibbonPanel( self.rb_page_dados, wx.ID_ANY, u"Registro" , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb_registro = rb.RibbonButtonBar( self.rb_panel_registro, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb_registro.AddSimpleButton( wx.ID_SAVE, u"Gravar", wx.Bitmap( u"icons/ac_confirmar_32x32.png", wx.BITMAP_TYPE_ANY ), u"Grava modificações")
		self.rbb_registro.AddSimpleButton( wx.ID_CANCEL, u"Cancelar", wx.Bitmap( u"icons/ac_cancelar_32x32.png", wx.BITMAP_TYPE_ANY ), wx.EmptyString)
		self.rb_panel_documento = rb.RibbonPanel( self.rb_page_dados, wx.ID_ANY, u"Documento" , wx.NullBitmap , wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE )
		self.rbb_documento = rb.RibbonButtonBar( self.rb_panel_documento, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.rbb_documento.AddSimpleButton( wx.ID_EXECUTE, u"Gerar", wx.Bitmap( u"icons/ac_documento_32x32.png", wx.BITMAP_TYPE_ANY ), u"Gerar documento")
		self.rbb_documento.AddSimpleButton( wx.ID_PRINT, u"Imprimir", wx.Bitmap( u"icons/ac_imprimir_32x32.png", wx.BITMAP_TYPE_ANY ), u"Imprimir documento gerado")
		self.ribbon_contrato.Realize()

		lay_ribbon.Add( self.ribbon_contrato, 1, wx.EXPAND, 1 )


		lay_tela.Add( lay_ribbon, 0, wx.EXPAND, 1 )

		lay_corpo = wx.BoxSizer( wx.VERTICAL )

		self.nb_contrato = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pn_contrato = wx.Panel( self.nb_contrato, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_contrato = wx.BoxSizer( wx.HORIZONTAL )

		lay_ctr_label_01 = wx.BoxSizer( wx.VERTICAL )

		self.lb_ctr_contrato = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Contrato:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_contrato.Wrap( -1 )

		lay_ctr_label_01.Add( self.lb_ctr_contrato, 0, wx.ALL, 1 )

		self.lb_unidade = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Unidade:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_unidade.Wrap( -1 )

		lay_ctr_label_01.Add( self.lb_unidade, 0, wx.ALL, 1 )

		self.lb_ctr_pessoa = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Pessoa:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_pessoa.Wrap( -1 )

		lay_ctr_label_01.Add( self.lb_ctr_pessoa, 0, wx.ALL, 1 )

		self.lb_ctr_vigencia = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Vigência:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_vigencia.Wrap( -1 )

		lay_ctr_label_01.Add( self.lb_ctr_vigencia, 0, wx.ALL, 1 )


		lay_contrato.Add( lay_ctr_label_01, 0, wx.EXPAND, 5 )

		lay_ctr_campos_01 = wx.BoxSizer( wx.VERTICAL )

		lay_ctr_operacao = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ctr_contrato = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,23 ), 0 )
		self.tc_ctr_contrato.SetMaxLength( 10 )
		self.tc_ctr_contrato.Enable( False )

		lay_ctr_operacao.Add( self.tc_ctr_contrato, 0, wx.ALL, 1 )

		self.lb_ctr_operacao = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Operação:", wx.DefaultPosition, wx.Size( 100,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_operacao.Wrap( -1 )

		lay_ctr_operacao.Add( self.lb_ctr_operacao, 0, wx.ALL, 1 )

		self.tc_ctr_operacao = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,23 ), 0 )
		self.tc_ctr_operacao.SetMaxLength( 3 )
		self.tc_ctr_operacao.Enable( False )

		lay_ctr_operacao.Add( self.tc_ctr_operacao, 0, wx.ALL, 1 )

		self.bt_ctr_loc_operacao = wx.BitmapButton( self.pn_contrato, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ctr_loc_operacao.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_loc_operacao.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_loc_operacao.Enable( False )

		lay_ctr_operacao.Add( self.bt_ctr_loc_operacao, 0, wx.ALIGN_CENTER, 1 )


		lay_ctr_campos_01.Add( lay_ctr_operacao, 0, wx.EXPAND, 1 )

		lay_unidade = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ctr_unidade = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,23 ), 0 )
		self.tc_ctr_unidade.SetMaxLength( 4 )
		self.tc_ctr_unidade.Enable( False )

		lay_unidade.Add( self.tc_ctr_unidade, 0, wx.ALL, 1 )

		self.tc_ctr_nome_unidade = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 320,23 ), 0 )
		self.tc_ctr_nome_unidade.Enable( False )

		lay_unidade.Add( self.tc_ctr_nome_unidade, 0, wx.ALL, 1 )

		self.bt_ctr_unidade = wx.BitmapButton( self.pn_contrato, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ctr_unidade.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_unidade.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_unidade.Enable( False )

		lay_unidade.Add( self.bt_ctr_unidade, 0, wx.ALL, 1 )


		lay_ctr_campos_01.Add( lay_unidade, 1, wx.EXPAND, 1 )

		lay_pessoa = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ctr_pessoa = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,23 ), 0 )
		self.tc_ctr_pessoa.SetMaxLength( 6 )
		self.tc_ctr_pessoa.Enable( False )

		lay_pessoa.Add( self.tc_ctr_pessoa, 0, wx.ALL, 1 )

		self.tc_ctr_nome_pessoa = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,23 ), 0 )
		self.tc_ctr_nome_pessoa.Enable( False )

		lay_pessoa.Add( self.tc_ctr_nome_pessoa, 0, wx.ALL, 1 )

		self.bt_ctr_loc_pessoa = wx.BitmapButton( self.pn_contrato, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ctr_loc_pessoa.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_loc_pessoa.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_loc_pessoa.Enable( False )

		lay_pessoa.Add( self.bt_ctr_loc_pessoa, 0, wx.ALL, 1 )


		lay_ctr_campos_01.Add( lay_pessoa, 0, wx.EXPAND, 1 )

		lay_vigencia = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ctr_vigencia = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,23 ), 0 )
		self.tc_ctr_vigencia.SetMaxLength( 3 )
		self.tc_ctr_vigencia.Enable( False )

		lay_vigencia.Add( self.tc_ctr_vigencia, 0, wx.ALL, 1 )

		cb_ctr_vigenciaChoices = [ u"dia(s)", u"mês(es)", u"ano(s)" ]
		self.cb_ctr_vigencia = wx.ComboBox( self.pn_contrato, wx.ID_ANY, u"mês(es)", wx.DefaultPosition, wx.Size( 110,23 ), cb_ctr_vigenciaChoices, 0 )
		self.cb_ctr_vigencia.SetSelection( 1 )
		self.cb_ctr_vigencia.Enable( False )

		lay_vigencia.Add( self.cb_ctr_vigencia, 0, wx.ALL, 1 )


		lay_ctr_campos_01.Add( lay_vigencia, 0, wx.EXPAND, 1 )


		lay_contrato.Add( lay_ctr_campos_01, 1, wx.EXPAND, 5 )

		lay_ctr_label_02 = wx.BoxSizer( wx.VERTICAL )

		self.lb_ctr_situacao = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Situação:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_situacao.Wrap( -1 )

		lay_ctr_label_02.Add( self.lb_ctr_situacao, 0, wx.ALL, 1 )

		self.lb_ctr_dt_emissao = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Data de emissão:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_dt_emissao.Wrap( -1 )

		lay_ctr_label_02.Add( self.lb_ctr_dt_emissao, 0, wx.ALL, 1 )

		self.lb_ctr_dt_inicio = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Data de início:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_dt_inicio.Wrap( -1 )

		lay_ctr_label_02.Add( self.lb_ctr_dt_inicio, 0, wx.ALL, 1 )

		self.lb_ctr_dt_termino = wx.StaticText( self.pn_contrato, wx.ID_ANY, u"Data de término:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_dt_termino.Wrap( -1 )

		lay_ctr_label_02.Add( self.lb_ctr_dt_termino, 0, wx.ALL, 1 )


		lay_contrato.Add( lay_ctr_label_02, 0, wx.EXPAND, 1 )

		lay_ctr_campos_02 = wx.BoxSizer( wx.VERTICAL )

		cb_ctr_situacaoChoices = [ u"Ativo", u"Análise", u"Bloqueado", u"Saneamento", u"Encerrado", u"Cancelado" ]
		self.cb_ctr_situacao = wx.ComboBox( self.pn_contrato, wx.ID_ANY, u"Ativo", wx.DefaultPosition, wx.Size( 120,23 ), cb_ctr_situacaoChoices, 0 )
		self.cb_ctr_situacao.SetSelection( 0 )
		self.cb_ctr_situacao.Enable( False )

		lay_ctr_campos_02.Add( self.cb_ctr_situacao, 0, wx.ALL, 1 )

		self.tc_ctr_dt_emissao = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,23 ), 0 )
		self.tc_ctr_dt_emissao.Enable( False )

		lay_ctr_campos_02.Add( self.tc_ctr_dt_emissao, 0, wx.ALL, 1 )

		lay_dt_inicio = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ctr_dt_inicio = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,23 ), 0 )
		self.tc_ctr_dt_inicio.Enable( False )

		lay_dt_inicio.Add( self.tc_ctr_dt_inicio, 0, wx.ALL, 1 )

		self.bt_ctr_dt_inicio = wx.BitmapButton( self.pn_contrato, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ctr_dt_inicio.SetBitmap( wx.Bitmap( u"icons/ac_calendario_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_dt_inicio.SetBitmapDisabled( wx.Bitmap( u"icons/ac_calendario_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_dt_inicio.Enable( False )

		lay_dt_inicio.Add( self.bt_ctr_dt_inicio, 0, wx.ALL, 1 )


		lay_ctr_campos_02.Add( lay_dt_inicio, 0, wx.EXPAND, 1 )

		lay_dt_termino = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_ctr_dt_termino = wx.TextCtrl( self.pn_contrato, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,23 ), 0 )
		self.tc_ctr_dt_termino.Enable( False )

		lay_dt_termino.Add( self.tc_ctr_dt_termino, 0, wx.ALL, 1 )

		self.bt_ctr_dt_termino = wx.BitmapButton( self.pn_contrato, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_ctr_dt_termino.SetBitmap( wx.Bitmap( u"icons/ac_calendario_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_dt_termino.SetBitmapDisabled( wx.Bitmap( u"icons/ac_calendario_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_ctr_dt_termino.Enable( False )

		lay_dt_termino.Add( self.bt_ctr_dt_termino, 0, wx.ALL, 1 )


		lay_ctr_campos_02.Add( lay_dt_termino, 0, wx.EXPAND, 1 )


		lay_contrato.Add( lay_ctr_campos_02, 1, wx.EXPAND, 5 )


		self.pn_contrato.SetSizer( lay_contrato )
		self.pn_contrato.Layout()
		lay_contrato.Fit( self.pn_contrato )
		self.nb_contrato.AddPage( self.pn_contrato, u"Principal", True )
		self.pn_valores = wx.Panel( self.nb_contrato, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_valores = wx.BoxSizer( wx.HORIZONTAL )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.lb_ctr_valor = wx.StaticText( self.pn_valores, wx.ID_ANY, u"Valor Total:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_ctr_valor.Wrap( -1 )

		bSizer34.Add( self.lb_ctr_valor, 0, wx.ALL, 1 )


		lay_valores.Add( bSizer34, 0, wx.EXPAND, 1 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.tc_ctr_valor = wx.TextCtrl( self.pn_valores, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,23 ), wx.TE_RIGHT )
		self.tc_ctr_valor.Enable( False )

		bSizer35.Add( self.tc_ctr_valor, 0, wx.ALL, 1 )


		lay_valores.Add( bSizer35, 1, wx.EXPAND, 5 )


		self.pn_valores.SetSizer( lay_valores )
		self.pn_valores.Layout()
		lay_valores.Fit( self.pn_valores )
		self.nb_contrato.AddPage( self.pn_valores, u"Valores", False )
		self.pn_abrangencia = wx.Panel( self.nb_contrato, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_abrangencia = wx.BoxSizer( wx.HORIZONTAL )

		lay_contratante = wx.StaticBoxSizer( wx.StaticBox( self.pn_abrangencia, wx.ID_ANY, u"Contratantes" ), wx.VERTICAL )


		lay_abrangencia.Add( lay_contratante, 1, wx.EXPAND, 5 )


		lay_abrangencia.Add( ( 5, 0), 0, wx.EXPAND, 5 )

		lay_contratados = wx.StaticBoxSizer( wx.StaticBox( self.pn_abrangencia, wx.ID_ANY, u"Contratados" ), wx.VERTICAL )


		lay_abrangencia.Add( lay_contratados, 1, wx.EXPAND, 5 )


		self.pn_abrangencia.SetSizer( lay_abrangencia )
		self.pn_abrangencia.Layout()
		lay_abrangencia.Fit( self.pn_abrangencia )
		self.nb_contrato.AddPage( self.pn_abrangencia, u"Abrangência", False )

		lay_corpo.Add( self.nb_contrato, 1, wx.EXPAND |wx.ALL, 1 )

		lay_registro = wx.BoxSizer( wx.VERTICAL )

		lay_grid = wx.BoxSizer( wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.VERTICAL )

		self.gd_ctr_itens = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gd_ctr_itens.CreateGrid( 0, 7 )
		self.gd_ctr_itens.EnableEditing( False )
		self.gd_ctr_itens.EnableGridLines( True )
		self.gd_ctr_itens.EnableDragGridSize( False )
		self.gd_ctr_itens.SetMargins( 0, 0 )

		# Columns
		self.gd_ctr_itens.SetColSize( 0, 50 )
		self.gd_ctr_itens.SetColSize( 1, 90 )
		self.gd_ctr_itens.SetColSize( 2, 120 )
		self.gd_ctr_itens.SetColSize( 3, 350 )
		self.gd_ctr_itens.SetColSize( 4, 100 )
		self.gd_ctr_itens.SetColSize( 5, 100 )
		self.gd_ctr_itens.SetColSize( 6, 150 )
		self.gd_ctr_itens.EnableDragColMove( False )
		self.gd_ctr_itens.EnableDragColSize( True )
		self.gd_ctr_itens.SetColLabelSize( 30 )
		self.gd_ctr_itens.SetColLabelValue( 0, u"#" )
		self.gd_ctr_itens.SetColLabelValue( 1, u"Código" )
		self.gd_ctr_itens.SetColLabelValue( 2, u"Tipo" )
		self.gd_ctr_itens.SetColLabelValue( 3, u"Descrição" )
		self.gd_ctr_itens.SetColLabelValue( 4, u"Quantidade" )
		self.gd_ctr_itens.SetColLabelValue( 5, u"V.Unitário" )
		self.gd_ctr_itens.SetColLabelValue( 6, u"V.Total" )
		self.gd_ctr_itens.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gd_ctr_itens.EnableDragRowSize( True )
		self.gd_ctr_itens.SetRowLabelSize( 30 )
		self.gd_ctr_itens.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gd_ctr_itens.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer17.Add( self.gd_ctr_itens, 1, wx.EXPAND, 1 )


		lay_grid.Add( bSizer17, 1, wx.EXPAND, 5 )

		lay_grid_botoes = wx.BoxSizer( wx.HORIZONTAL )

		self.bt_item_consultar = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_consultar.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_consultar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_consultar.Enable( False )

		lay_grid_botoes.Add( self.bt_item_consultar, 0, wx.ALL, 1 )

		self.bt_item_adicionar = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_adicionar.SetBitmap( wx.Bitmap( u"icons/ac_adicionar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_adicionar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_adicionar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_adicionar.Enable( False )

		lay_grid_botoes.Add( self.bt_item_adicionar, 0, wx.ALL, 1 )

		self.bt_item_editar = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_editar.SetBitmap( wx.Bitmap( u"icons/ac_editar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_editar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_editar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_editar.Enable( False )

		lay_grid_botoes.Add( self.bt_item_editar, 0, wx.ALL, 1 )

		self.bt_item_excluir = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_excluir.SetBitmap( wx.Bitmap( u"icons/ac_lixeira_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_excluir.SetBitmapDisabled( wx.Bitmap( u"icons/ac_lixeira_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_excluir.Enable( False )

		lay_grid_botoes.Add( self.bt_item_excluir, 0, wx.ALL, 1 )

		self.bt_item_confirmar = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_confirmar.SetBitmap( wx.Bitmap( u"icons/ac_confirmar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_confirmar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_confirmar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_confirmar.Enable( False )

		lay_grid_botoes.Add( self.bt_item_confirmar, 0, wx.ALL, 1 )

		self.bt_item_cancelar = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_cancelar.SetBitmap( wx.Bitmap( u"icons/ac_cancelar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_cancelar.SetBitmapDisabled( wx.Bitmap( u"icons/ac_cancelar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_cancelar.Enable( False )

		lay_grid_botoes.Add( self.bt_item_cancelar, 0, wx.ALL, 1 )


		lay_grid.Add( lay_grid_botoes, 0, wx.EXPAND, 1 )


		lay_registro.Add( lay_grid, 1, wx.EXPAND, 5 )

		lay_detalhes = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pn_dados = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_dados = wx.BoxSizer( wx.HORIZONTAL )

		lay_dados_label_01 = wx.BoxSizer( wx.VERTICAL )

		self.lb_item_tipo = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Tipo do item:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_tipo.Wrap( -1 )

		lay_dados_label_01.Add( self.lb_item_tipo, 0, wx.ALL, 1 )

		self.lb_item_coditem = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Código:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_item_coditem.Wrap( -1 )

		lay_dados_label_01.Add( self.lb_item_coditem, 0, wx.ALL, 1 )

		self.lb_item_descricao = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.Size( 150,78 ), wx.ALIGN_RIGHT )
		self.lb_item_descricao.Wrap( -1 )

		lay_dados_label_01.Add( self.lb_item_descricao, 0, wx.ALL, 1 )

		self.lb_item_quantidade = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Quantidade:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_quantidade.Wrap( -1 )

		lay_dados_label_01.Add( self.lb_item_quantidade, 0, wx.ALL, 1 )

		self.lb_item_vl_unitario = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Valor unitário:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_vl_unitario.Wrap( -1 )

		lay_dados_label_01.Add( self.lb_item_vl_unitario, 0, wx.ALL, 1 )

		self.lb_item_imobilizado = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Imobilizado:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_imobilizado.Wrap( -1 )

		lay_dados_label_01.Add( self.lb_item_imobilizado, 0, wx.ALL, 1 )


		lay_dados.Add( lay_dados_label_01, 0, wx.EXPAND, 1 )

		lay_dados_campos_01 = wx.BoxSizer( wx.VERTICAL )

		lay_tipo = wx.BoxSizer( wx.HORIZONTAL )

		cb_item_tipoChoices = [ u"Serviço", u"Material" ]
		self.cb_item_tipo = wx.ComboBox( self.pn_dados, wx.ID_ANY, u"Serviço", wx.DefaultPosition, wx.Size( 100,23 ), cb_item_tipoChoices, 0 )
		self.cb_item_tipo.SetSelection( 0 )
		self.cb_item_tipo.Enable( False )

		lay_tipo.Add( self.cb_item_tipo, 0, wx.ALL, 1 )

		self.lb_item_codigo = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Sequencia:", wx.DefaultPosition, wx.Size( 150,23 ), wx.ALIGN_RIGHT )
		self.lb_item_codigo.Wrap( -1 )

		lay_tipo.Add( self.lb_item_codigo, 0, wx.ALL, 1 )

		self.tc_item_codigo = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,23 ), 0 )
		self.tc_item_codigo.Enable( False )

		lay_tipo.Add( self.tc_item_codigo, 0, wx.ALL, 1 )


		lay_dados_campos_01.Add( lay_tipo, 1, wx.EXPAND, 1 )

		lay_codigo_item = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_coditem = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_item_coditem.SetMaxLength( 6 )
		self.tc_item_coditem.Enable( False )

		lay_codigo_item.Add( self.tc_item_coditem, 0, wx.ALL, 1 )

		self.tc_item_nome = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,26 ), 0 )
		self.tc_item_nome.Enable( False )

		lay_codigo_item.Add( self.tc_item_nome, 0, wx.ALL, 1 )

		self.bt_item_loc_codigo = wx.BitmapButton( self.pn_dados, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_loc_codigo.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_codigo.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_codigo.Enable( False )

		lay_codigo_item.Add( self.bt_item_loc_codigo, 0, wx.ALL, 1 )


		lay_dados_campos_01.Add( lay_codigo_item, 0, wx.EXPAND, 1 )

		self.tc_item_descricao = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 495,78 ), wx.TE_MULTILINE )
		self.tc_item_descricao.Enable( False )

		lay_dados_campos_01.Add( self.tc_item_descricao, 0, wx.ALL, 1 )

		self.tc_item_quantidade = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,26 ), 0 )
		self.tc_item_quantidade.Enable( False )

		lay_dados_campos_01.Add( self.tc_item_quantidade, 0, wx.ALL, 1 )

		lay_valor = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_val_unitario = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,26 ), wx.TE_RIGHT )
		self.tc_item_val_unitario.Enable( False )

		lay_valor.Add( self.tc_item_val_unitario, 0, wx.ALL, 1 )

		self.lb_item_val_total = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Valor total:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_val_total.Wrap( -1 )

		lay_valor.Add( self.lb_item_val_total, 0, wx.ALL, 1 )

		self.tc_item_val_total = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,26 ), wx.TE_RIGHT )
		self.tc_item_val_total.Enable( False )

		lay_valor.Add( self.tc_item_val_total, 0, wx.ALL, 1 )

		self.lb_item_moeda = wx.StaticText( self.pn_dados, wx.ID_ANY, u"Moeda:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_moeda.Wrap( -1 )

		lay_valor.Add( self.lb_item_moeda, 0, wx.ALL, 1 )

		self.tc_item_moeda = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,26 ), wx.TE_CENTER )
		self.tc_item_moeda.Enable( False )

		lay_valor.Add( self.tc_item_moeda, 0, wx.ALL, 1 )


		lay_dados_campos_01.Add( lay_valor, 0, wx.EXPAND, 1 )

		lay_imobilizado = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_imobilizado = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_item_imobilizado.SetMaxLength( 6 )
		self.tc_item_imobilizado.Enable( False )

		lay_imobilizado.Add( self.tc_item_imobilizado, 0, wx.ALL, 1 )

		self.tc_item_imob_nome = wx.TextCtrl( self.pn_dados, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,26 ), 0 )
		self.tc_item_imob_nome.Enable( False )

		lay_imobilizado.Add( self.tc_item_imob_nome, 0, wx.ALL, 1 )

		self.bt_item_loc_imob = wx.BitmapButton( self.pn_dados, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_loc_imob.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_imob.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_imob.Enable( False )

		lay_imobilizado.Add( self.bt_item_loc_imob, 0, wx.ALL, 1 )


		lay_dados_campos_01.Add( lay_imobilizado, 0, wx.EXPAND, 1 )


		lay_dados.Add( lay_dados_campos_01, 1, wx.EXPAND, 5 )


		self.pn_dados.SetSizer( lay_dados )
		self.pn_dados.Layout()
		lay_dados.Fit( self.pn_dados )
		self.m_notebook1.AddPage( self.pn_dados, u"Dados Básicos", True )
		self.pn_financeiro = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		lay_financeiro = wx.BoxSizer( wx.HORIZONTAL )

		lay_finan_label_01 = wx.BoxSizer( wx.VERTICAL )

		self.lb_item_form_pgto = wx.StaticText( self.pn_financeiro, wx.ID_ANY, u"Forma de pagamento:", wx.DefaultPosition, wx.Size( 200,26 ), wx.ALIGN_RIGHT )
		self.lb_item_form_pgto.Wrap( -1 )

		lay_finan_label_01.Add( self.lb_item_form_pgto, 0, wx.ALL, 1 )

		self.tc_item_cond_pgto = wx.StaticText( self.pn_financeiro, wx.ID_ANY, u"Condição de pagamento:", wx.DefaultPosition, wx.Size( 200,26 ), wx.ALIGN_RIGHT )
		self.tc_item_cond_pgto.Wrap( -1 )

		lay_finan_label_01.Add( self.tc_item_cond_pgto, 0, wx.ALL, 1 )

		self.tc_item_conta_bancaria = wx.StaticText( self.pn_financeiro, wx.ID_ANY, u"Conta bancária:", wx.DefaultPosition, wx.Size( 200,26 ), wx.ALIGN_RIGHT )
		self.tc_item_conta_bancaria.Wrap( -1 )

		lay_finan_label_01.Add( self.tc_item_conta_bancaria, 0, wx.ALL, 1 )

		self.lb_item_cartao = wx.StaticText( self.pn_financeiro, wx.ID_ANY, u"Cartão:", wx.DefaultPosition, wx.Size( 200,26 ), wx.ALIGN_RIGHT )
		self.lb_item_cartao.Wrap( -1 )

		lay_finan_label_01.Add( self.lb_item_cartao, 0, wx.ALL, 1 )


		lay_financeiro.Add( lay_finan_label_01, 0, wx.EXPAND, 1 )

		lay_finan_campos_01 = wx.BoxSizer( wx.VERTICAL )

		lay_form_pgto = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_form_pgto = wx.TextCtrl( self.pn_financeiro, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		self.tc_item_form_pgto.SetMaxLength( 3 )
		self.tc_item_form_pgto.Enable( False )

		lay_form_pgto.Add( self.tc_item_form_pgto, 0, wx.ALL, 1 )

		self.bt_item_loc_form_pgto = wx.BitmapButton( self.pn_financeiro, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_loc_form_pgto.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_form_pgto.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_form_pgto.Enable( False )

		lay_form_pgto.Add( self.bt_item_loc_form_pgto, 0, wx.ALL, 1 )


		lay_finan_campos_01.Add( lay_form_pgto, 0, wx.EXPAND, 5 )

		lay_cond_pgto = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_cond_pgto = wx.TextCtrl( self.pn_financeiro, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 70,26 ), 0 )
		self.tc_item_cond_pgto.SetMaxLength( 4 )
		self.tc_item_cond_pgto.Enable( False )

		lay_cond_pgto.Add( self.tc_item_cond_pgto, 0, wx.ALL, 1 )

		self.bt_item_loc_cond_pgto = wx.BitmapButton( self.pn_financeiro, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_loc_cond_pgto.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_cond_pgto.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_cond_pgto.Enable( False )

		lay_cond_pgto.Add( self.bt_item_loc_cond_pgto, 0, wx.ALL, 1 )

		cb_item_tipo_cpgtoChoices = [ u"Antecipado", u"Postecipado" ]
		self.cb_item_tipo_cpgto = wx.ComboBox( self.pn_financeiro, wx.ID_ANY, u"Antecipado", wx.DefaultPosition, wx.Size( 150,26 ), cb_item_tipo_cpgtoChoices, 0 )
		self.cb_item_tipo_cpgto.SetSelection( 0 )
		self.cb_item_tipo_cpgto.Enable( False )

		lay_cond_pgto.Add( self.cb_item_tipo_cpgto, 0, wx.ALL, 1 )

		self.lb_item_dia_vcto = wx.StaticText( self.pn_financeiro, wx.ID_ANY, u"Dia vencimento:", wx.DefaultPosition, wx.Size( 150,26 ), wx.ALIGN_RIGHT )
		self.lb_item_dia_vcto.Wrap( -1 )

		lay_cond_pgto.Add( self.lb_item_dia_vcto, 0, wx.ALL, 1 )

		self.tc_item_dia_vcto = wx.TextCtrl( self.pn_financeiro, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 40,26 ), 0 )
		self.tc_item_dia_vcto.SetMaxLength( 2 )
		self.tc_item_dia_vcto.Enable( False )

		lay_cond_pgto.Add( self.tc_item_dia_vcto, 0, wx.ALL, 1 )


		lay_finan_campos_01.Add( lay_cond_pgto, 0, wx.EXPAND, 1 )

		lay_conta_bancaria = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_conta_bancaria = wx.TextCtrl( self.pn_financeiro, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		self.tc_item_conta_bancaria.SetMaxLength( 4 )
		self.tc_item_conta_bancaria.Enable( False )

		lay_conta_bancaria.Add( self.tc_item_conta_bancaria, 0, wx.ALL, 1 )

		self.bt_item_loc_conta_banc = wx.BitmapButton( self.pn_financeiro, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_loc_conta_banc.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_conta_banc.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_conta_banc.Enable( False )

		lay_conta_bancaria.Add( self.bt_item_loc_conta_banc, 0, wx.ALL, 1 )


		lay_finan_campos_01.Add( lay_conta_bancaria, 0, wx.EXPAND, 1 )

		lay_cartao = wx.BoxSizer( wx.HORIZONTAL )

		self.tc_item_cartao = wx.TextCtrl( self.pn_financeiro, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,26 ), 0 )
		self.tc_item_cartao.SetMaxLength( 4 )
		self.tc_item_cartao.Enable( False )

		lay_cartao.Add( self.tc_item_cartao, 0, wx.ALL, 1 )

		self.bt_item_loc_cartao = wx.BitmapButton( self.pn_financeiro, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.bt_item_loc_cartao.SetBitmap( wx.Bitmap( u"icons/ac_buscar_16x16.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_cartao.SetBitmapDisabled( wx.Bitmap( u"icons/ac_buscar_16x16_inat.png", wx.BITMAP_TYPE_ANY ) )
		self.bt_item_loc_cartao.Enable( False )

		lay_cartao.Add( self.bt_item_loc_cartao, 0, wx.ALL, 1 )


		lay_finan_campos_01.Add( lay_cartao, 0, wx.EXPAND, 1 )


		lay_financeiro.Add( lay_finan_campos_01, 1, wx.EXPAND, 5 )

		lay_vencimentos = wx.StaticBoxSizer( wx.StaticBox( self.pn_financeiro, wx.ID_ANY, u"Vencimentos" ), wx.VERTICAL )

		self.gd_item_vencimento = wx.grid.Grid( lay_vencimentos.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )

		# Grid
		self.gd_item_vencimento.CreateGrid( 1, 2 )
		self.gd_item_vencimento.EnableEditing( True )
		self.gd_item_vencimento.EnableGridLines( True )
		self.gd_item_vencimento.EnableDragGridSize( False )
		self.gd_item_vencimento.SetMargins( 0, 0 )

		# Columns
		self.gd_item_vencimento.SetColSize( 0, 50 )
		self.gd_item_vencimento.SetColSize( 1, 100 )
		self.gd_item_vencimento.EnableDragColMove( False )
		self.gd_item_vencimento.EnableDragColSize( True )
		self.gd_item_vencimento.SetColLabelSize( 30 )
		self.gd_item_vencimento.SetColLabelValue( 0, u"Nº" )
		self.gd_item_vencimento.SetColLabelValue( 1, u"Vencimento" )
		self.gd_item_vencimento.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gd_item_vencimento.EnableDragRowSize( True )
		self.gd_item_vencimento.SetRowLabelSize( 1 )
		self.gd_item_vencimento.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gd_item_vencimento.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		lay_vencimentos.Add( self.gd_item_vencimento, 0, wx.EXPAND, 5 )


		lay_financeiro.Add( lay_vencimentos, 0, wx.EXPAND, 5 )


		self.pn_financeiro.SetSizer( lay_financeiro )
		self.pn_financeiro.Layout()
		lay_financeiro.Fit( self.pn_financeiro )
		self.m_notebook1.AddPage( self.pn_financeiro, u"Financeiro", False )
		self.pn_tributario = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer19 = wx.BoxSizer( wx.VERTICAL )


		self.pn_tributario.SetSizer( bSizer19 )
		self.pn_tributario.Layout()
		bSizer19.Fit( self.pn_tributario )
		self.m_notebook1.AddPage( self.pn_tributario, u"Tributário", False )

		lay_detalhes.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		lay_registro.Add( lay_detalhes, 1, wx.EXPAND, 5 )


		lay_corpo.Add( lay_registro, 1, wx.EXPAND, 5 )


		lay_tela.Add( lay_corpo, 0, wx.EXPAND, 5 )


		self.SetSizer( lay_tela )
		self.Layout()
		self.sb_contrato = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ctr_consultar, id = wx.ID_FIND )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ctr_adicionar, id = wx.ID_NEW )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ctr_editar, id = wx.ID_EDIT )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ctr_excluir, id = wx.ID_DELETE )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ctr_confirmar, id = wx.ID_SAVE )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ctr_cancelar, id = wx.ID_CANCEL )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ctr_gerar_doc, id = wx.ID_EXECUTE )
		self.Bind( rb.EVT_RIBBONBUTTONBAR_CLICKED, self.ac_ctr_imprimir, id = wx.ID_PRINT )
		self.bt_ctr_loc_operacao.Bind( wx.EVT_BUTTON, self.ac_loc_operacao )
		self.bt_ctr_unidade.Bind( wx.EVT_BUTTON, self.ac_loc_unidade )
		self.bt_ctr_loc_pessoa.Bind( wx.EVT_BUTTON, self.ac_loc_pessoa )
		self.tc_ctr_vigencia.Bind( wx.EVT_KILL_FOCUS, self.off_focus_vigencia )
		self.tc_ctr_vigencia.Bind( wx.EVT_SET_FOCUS, self.on_focus_vigencia )
		self.cb_ctr_vigencia.Bind( wx.EVT_COMBOBOX, self.ac_ctr_tp_vigencia )
		self.bt_ctr_dt_inicio.Bind( wx.EVT_BUTTON, self.ac_dt_inicio )
		self.bt_ctr_dt_termino.Bind( wx.EVT_BUTTON, self.ac_dt_termino )
		self.bt_item_consultar.Bind( wx.EVT_BUTTON, self.ac_item_consultar )
		self.bt_item_adicionar.Bind( wx.EVT_BUTTON, self.ac_item_adicionar )
		self.bt_item_editar.Bind( wx.EVT_BUTTON, self.ac_item_editar )
		self.bt_item_excluir.Bind( wx.EVT_BUTTON, self.ac_item_excluir )
		self.bt_item_confirmar.Bind( wx.EVT_BUTTON, self.ac_item_confirmar )
		self.bt_item_cancelar.Bind( wx.EVT_BUTTON, self.ac_item_cancelar )
		self.bt_item_loc_codigo.Bind( wx.EVT_BUTTON, self.ac_loc_item )
		self.tc_item_quantidade.Bind( wx.EVT_KILL_FOCUS, self.off_focus_qtde )
		self.tc_item_quantidade.Bind( wx.EVT_SET_FOCUS, self.on_focus_qtde )
		self.tc_item_val_unitario.Bind( wx.EVT_KILL_FOCUS, self.off_focus_vunit )
		self.tc_item_val_unitario.Bind( wx.EVT_SET_FOCUS, self.on_focus_vunit )
		self.tc_item_val_total.Bind( wx.EVT_KILL_FOCUS, self.off_focus_vtotal )
		self.tc_item_val_total.Bind( wx.EVT_SET_FOCUS, self.on_focus_vtotal )
		self.tc_item_imobilizado.Bind( wx.EVT_KILL_FOCUS, self.off_focus_imob )
		self.tc_item_imobilizado.Bind( wx.EVT_SET_FOCUS, self.on_focus_imob )
		self.bt_item_loc_imob.Bind( wx.EVT_BUTTON, self.ac_loc_imobilizado )
		self.bt_item_loc_form_pgto.Bind( wx.EVT_BUTTON, self.ac_loc_form_pgto )
		self.bt_item_loc_cond_pgto.Bind( wx.EVT_BUTTON, self.ac_loc_cond_pgto )
		self.bt_item_loc_conta_banc.Bind( wx.EVT_BUTTON, self.ac_loc_conta_bancaria )
		self.bt_item_loc_cartao.Bind( wx.EVT_BUTTON, self.ac_loc_cartao )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def ac_ctr_consultar( self, event ):
		event.Skip()

	def ac_ctr_adicionar( self, event ):
		event.Skip()

	def ac_ctr_editar( self, event ):
		event.Skip()

	def ac_ctr_excluir( self, event ):
		event.Skip()

	def ac_ctr_confirmar( self, event ):
		event.Skip()

	def ac_ctr_cancelar( self, event ):
		event.Skip()

	def ac_ctr_gerar_doc( self, event ):
		event.Skip()

	def ac_ctr_imprimir( self, event ):
		event.Skip()

	def ac_loc_operacao( self, event ):
		event.Skip()

	def ac_loc_unidade( self, event ):
		event.Skip()

	def ac_loc_pessoa( self, event ):
		event.Skip()

	def off_focus_vigencia( self, event ):
		event.Skip()

	def on_focus_vigencia( self, event ):
		event.Skip()

	def ac_ctr_tp_vigencia( self, event ):
		event.Skip()

	def ac_dt_inicio( self, event ):
		event.Skip()

	def ac_dt_termino( self, event ):
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

	def ac_loc_item( self, event ):
		event.Skip()

	def off_focus_qtde( self, event ):
		event.Skip()

	def on_focus_qtde( self, event ):
		event.Skip()

	def off_focus_vunit( self, event ):
		event.Skip()

	def on_focus_vunit( self, event ):
		event.Skip()

	def off_focus_vtotal( self, event ):
		event.Skip()

	def on_focus_vtotal( self, event ):
		event.Skip()

	def off_focus_imob( self, event ):
		event.Skip()

	def on_focus_imob( self, event ):
		event.Skip()

	def ac_loc_imobilizado( self, event ):
		event.Skip()

	def ac_loc_form_pgto( self, event ):
		event.Skip()

	def ac_loc_cond_pgto( self, event ):
		event.Skip()

	def ac_loc_conta_bancaria( self, event ):
		event.Skip()

	def ac_loc_cartao( self, event ):
		event.Skip()


