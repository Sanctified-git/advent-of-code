use std::time::{Instant, Duration};
use std::fs::File;
use std::io::{BufReader, Read};
use std::path::Path;

/// Return the input file corresponding to a given filename as a list.
pub fn get_input(filename: &str, separator: Option<char>) -> Vec<String>{
    let path = Path::new("res").join(strip_name(filename) + ".txt");
    let mut buf_reader = BufReader::new(File::open(path).expect("Unable to open file"));
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents).expect("Unable to read file content");
    return contents.split(separator.unwrap_or('\n')).map(String::from).collect()
}

/// Remove path and extension from a given file path, returning only the file name.
pub fn strip_name(filename: &str) -> String {
    return Path::new(&filename).file_stem().unwrap().to_str().unwrap().to_string()
}

/// Basic timer class for use in advent-of-code
pub struct Timer {
    start_time: Instant,
    step_time: Option<Instant>
}

impl Timer {
    /// Report the elapsed time since last step
    pub fn step(&mut self, name: &str) {
        let elapsed_time: Duration;
        elapsed_time = self.step_time.unwrap_or(self.start_time).elapsed();
        self.step_time = Some(Instant::now());
        println!("Elapsed time for {} : {:?}", strip_name(name), elapsed_time);
    }

    /// Report the total elapsed time
    pub fn total(&self, name: &str) {
        let elapsed_time = self.start_time.elapsed();
        println!("Total elapsed time for {} : {:?}\n", strip_name(name), elapsed_time);
    }
}

/// Start a timer and return it
pub fn build_timer(name: &str) -> Timer {
    println!("Starting timer for {}", strip_name(name));
    let timer = Timer { start_time: Instant::now(), step_time: None };
    return timer
}
