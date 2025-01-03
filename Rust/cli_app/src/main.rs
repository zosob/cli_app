use std::env;
use std::fs; //File system

fn main() {
    let args: Vec<String> = env:: args().collect(); 
    let query: &String = &args[1];
    let filename :&String = &args[2];

    println!("Searching for {}", query);
    println!("In file: {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong!");

    println!("With text: \n{}",contents);
}
