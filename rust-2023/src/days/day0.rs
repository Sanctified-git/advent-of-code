use crate::utils;

fn compute_sum() {
	let input = utils::get_input(file!(), None);
	let mut part_one_sum = 0;
	let mut part_two_sum = 0;

	
	// PART ONE


	println!("The sum of calibration values is {}", part_one_sum);

	// PART TWO
	

	println!("The new sum of calibration values is {}", part_two_sum);
}

/// https://adventofcode.com/2023/day/0
pub fn main() {
	let t = utils::build_timer(file!());
	compute_sum();
	t.step(file!());
}
