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
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let mut results: Vec<&str> = Vec::new();

    for line in contents.lines(){
        if line.contains(query){
            results.push(line);

        }
    }
    results
}


#[cfg(test)]
mod tests{
    use super::*;

    #[test]
    fn one_result(){
        let query:&str = "duct";
        let contents: &str = "\
Rust:
safe, fast, productive.
Pick three.";
        assert_eq!(vec!["safe, fast, productive."], search(query, contents));
    }
}