use std::fs; //File system
use std::error::Error;



pub fn run(config: Config)-> Result<(), Box<dyn Error>>{
    let contents = fs::read_to_string(config.filename)?; //Automatically returns an error...

    println!("With text: \n{}",contents);
    Ok(())
}


pub struct Config{
    pub query : String,
    pub filename : String,
}

impl Config{ 
    pub fn new(args:&[String]) -> Result<Config, &str> {
        if args.len() < 3{
            return Err("not enough arguments");
        }
        let query: String = args[1].clone();
        let filename :String = args[2].clone();
        Ok( Config{query, filename})
    }
}
