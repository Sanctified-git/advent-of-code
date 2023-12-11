use std::time::Instant;
use std::fs::File;
use std::io::{BufReader, Read};
use std::path::Path;

/// Return the input file corresponding to a given filename as a list.
pub fn get_input(filename: &str, separator: Option<char>) -> Vec<String>{
    let path = Path::new("res").join(strip_name(filename) + ".txt");
    let mut buf_reader = BufReader::new(File::open(path).expect("Unable to open file"));
    let mut contents = String::new();
    let _ = buf_reader.read_to_string(&mut contents);
    return contents.split(separator.unwrap_or('\n')).map(String::from).collect()
}

/// Remove path and extension from a given file path, returning only the file name.
pub fn strip_name(filename: &str) -> String {
    return Path::new(&filename).file_stem().unwrap().to_str().unwrap().to_string()
}

/// Basic timer class for use in advent-of-code
pub struct Timer {
    start_time: Instant
}

impl Timer {
    /// Report the elapsed time
    pub fn step(self, name: &str) {
        let elapsed_time = self.start_time.elapsed();
        println!("Elapsed time for {} : {:?}\n", strip_name(name), elapsed_time);
    }
}

/// Start a timer and return it
pub fn build_timer(name: &str) -> Timer {
    println!("Starting timer for {}", strip_name(name));
    let timer = Timer { start_time: Instant::now() };
    return timer
}
