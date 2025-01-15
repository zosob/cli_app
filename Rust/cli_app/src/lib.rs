use std::fs; //File system
use std::error::Error;



pub fn run(config: Config)-> Result<(), Box<dyn Error>>{
    let contents = fs::read_to_string(config.filename)?; //Automatically returns an error...

    for line in search(&config.query, &contents){
        println!("Line found: {}", line);
    }
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
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let mut results: Vec<&str> = Vec::new();

    for line in contents.lines(){
        if line.contains(query){
            results.push(line);
        }
    }
    results
}

pub fn search_case_insensitive<'a>(query:&str,contents: &'a str,)->Vec<&'a str>{
    let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines(){
        if line.to_lowercase().contains(&query){
            results.push(line);
        }
    }
    results    
}


#[cfg(test)]
mod tests{
    use super::*;

    #[test]
    fn case_sensitive(){
        let query:&str = "duct";
        let contents: &str = "\
Rust:
safe, fast, productive.
Pick three
Duct tape.";
        assert_eq!(vec!["safe, fast, productive."], search(query, contents));
    }

    #[test]
    fn case_insensitive(){
        let query = "rUsT";
        let contents = "\
Rust:
safe, fast, productive.
Pick three.
Trust me.";

        assert_eq!(vec!["Rust:", "Trust me."], search_case_insensitive(query, contents));
    }
    
}

