use rust_utils::utils;

fn count_scratchcards() {
	let input = utils::get_input(file!(), None);
	let mut part_one_total = 0;
	let mut part_two_total = 0;

	// PART ONE
	for l in input.clone() {
		if !l.is_empty() {
			let mut matches = 0;
			let (winning_str, my_str) = l.split_once(": ").unwrap().1.split_once(" | ").unwrap();
			let winning_nums: Vec<i32> = winning_str.trim().replace("  ", " ").split(' ').map(
				|c| i32::from_str_radix(c.trim(), 10).unwrap()
			).collect();
			let my_nums: Vec<i32> = my_str.trim().replace("  ", " ").split(' ').map(
				|c| i32::from_str_radix(c.trim(), 10).unwrap()
			).collect();
	
			for num in my_nums {
				if winning_nums.contains(&num) { matches += 1;}
			}
			if matches > 0 { part_one_total += i32::pow(2, matches - 1); }
		}
	}

	println!("The pile of cards is worth {} points", part_one_total);

	// PART TWO
	

	println!(" {}", part_two_total);
}

/// https://adventofcode.com/2023/day/4
pub fn main() {
	let t = utils::build_timer(file!());
	count_scratchcards();
	t.step(file!());
}
