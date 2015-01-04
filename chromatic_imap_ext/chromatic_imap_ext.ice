//William K. Johnson 2013

module chromatic_imap_ext 
{ 
		
	//forward
	interface chromatic_node;
	
	//enumerations
	enum chromatic_error_level
	{
		celCritical ,
		celSystem ,
		celSilent ,
		celNoError
	};
	
	//types
	sequence<string> v_lines; 
	sequence<chromatic_node*> chromatic_node_seq;
	
	//exception classes
	exception chromatic_file_exception
	{ 
		string reason; 
		chromatic_error_level cel = celNoError;
	}; 
	
	//services
	interface chromatic_node
	{ 
		idempotent string name(); 
	}; 	

	interface chromatic_file extends chromatic_node 
	{ 
		idempotent v_lines read(); 
		idempotent void write( v_lines text ) throws chromatic_file_exception; 
	};	
	 
	interface chromatic_directory extends chromatic_node
	{ 
		idempotent chromatic_node_seq list();
	}; 
}; 

