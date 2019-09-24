///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyPanel1::MyPanel1( wxWindow* parent, wxWindowID id, const wxPoint& pos, const wxSize& size, long style, const wxString& name ) : wxPanel( parent, id, pos, size, style, name )
{
	wxBoxSizer* lay_body;
	lay_body = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxHORIZONTAL );

	wxBoxSizer* lay_modulos;
	lay_modulos = new wxBoxSizer( wxVERTICAL );

	wxBoxSizer* bSizer8;
	bSizer8 = new wxBoxSizer( wxVERTICAL );

	m_staticText1 = new wxStaticText( this, wxID_ANY, wxT("MÓDULOS"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText1->Wrap( -1 );
	bSizer8->Add( m_staticText1, 0, wxEXPAND, 5 );


	lay_modulos->Add( bSizer8, 0, wxEXPAND, 0 );

	wxBoxSizer* lay_bottons;
	lay_bottons = new wxBoxSizer( wxVERTICAL );

	m_button1 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxSize( 200,-1 ), 0 );
	lay_bottons->Add( m_button1, 0, wxALL, 5 );

	m_button2 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxSize( 200,-1 ), 0 );
	lay_bottons->Add( m_button2, 0, wxALL, 5 );

	m_button3 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxSize( 200,-1 ), 0 );
	lay_bottons->Add( m_button3, 0, wxALL, 5 );

	m_button4 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxSize( 200,-1 ), 0 );
	lay_bottons->Add( m_button4, 0, wxALL, 5 );

	m_button5 = new wxButton( this, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxSize( 200,-1 ), 0 );
	lay_bottons->Add( m_button5, 0, wxALL, 5 );


	lay_modulos->Add( lay_bottons, 1, wxEXPAND, 5 );


	bSizer5->Add( lay_modulos, 0, wxEXPAND, 1 );

	wxBoxSizer* lay_transacoes;
	lay_transacoes = new wxBoxSizer( wxVERTICAL );

	m_panel1 = new wxPanel( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxGridSizer* gSizer1;
	gSizer1 = new wxGridSizer( 8, 4, 5, 5 );

	m_button6 = new wxButton( m_panel1, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_button6, 0, wxEXPAND, 5 );

	m_button7 = new wxButton( m_panel1, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_button7, 0, wxEXPAND, 5 );

	m_button8 = new wxButton( m_panel1, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_button8, 0, wxEXPAND, 5 );

	m_button9 = new wxButton( m_panel1, wxID_ANY, wxT("MyButton"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer1->Add( m_button9, 0, wxEXPAND, 5 );


	m_panel1->SetSizer( gSizer1 );
	m_panel1->Layout();
	gSizer1->Fit( m_panel1 );
	lay_transacoes->Add( m_panel1, 1, wxEXPAND | wxALL, 0 );


	bSizer5->Add( lay_transacoes, 1, wxEXPAND, 1 );

	wxBoxSizer* lay_inform;
	lay_inform = new wxBoxSizer( wxVERTICAL );

	m_richText1 = new wxRichTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 200,-1 ), 0|wxVSCROLL|wxHSCROLL|wxNO_BORDER|wxWANTS_CHARS );
	lay_inform->Add( m_richText1, 1, wxEXPAND | wxALL, 5 );


	bSizer5->Add( lay_inform, 0, wxEXPAND, 1 );


	lay_body->Add( bSizer5, 1, wxEXPAND, 5 );


	this->SetSizer( lay_body );
	this->Layout();
}

MyPanel1::~MyPanel1()
{
}
