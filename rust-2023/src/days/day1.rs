use std::collections::HashMap;
use crate::utils;

fn compute_sum() {
	let input = utils::get_input(file!(), None);
	let (mut part_one_sum, mut part_two_sum): (u32, u32) = (0, 0);
	let digits: HashMap<&str, &str> = [
		("one", "o1e"),
		("two", "t2o"),
		("three", "t3e"),
		("four", "f4r"),
		("five", "f5e"),
		("six", "s6x"),
		("seven", "s7n"),
		("eight", "e8t"),
		("nine", "n9e")
	].into();
	
	// PART ONE
	for l in input.clone() {
		part_one_sum += get_calibration_value(l);
	}
	
	println!("The sum of calibration values is {}", part_one_sum);

	// PART TWO
	for l in input {
		let converted_line = convert_spelled_digits(l, &digits);
		part_two_sum += get_calibration_value(converted_line);
	}

	println!("The new sum of calibration values is {}", part_two_sum);
}

fn get_calibration_value(l: String) -> u32 {
	let ints: Vec<u32> = l.trim().chars().filter_map(
		|x| x.to_digit(10)
	).collect();
	return u32::from_str_radix((ints[0].to_string() + &ints[ints.len()-1].to_string()).as_str(),10).unwrap();
}

fn convert_spelled_digits(mut l: String, digits: &HashMap<&str, &str>) -> String {
	for i in digits {
		l = l.replace(i.0, i.1);
	}
	return l;
}

/// https://adventofcode.com/2023/day/1
pub fn main() {
	let t = utils::build_timer(file!());
	compute_sum();
	t.step(file!());
}
