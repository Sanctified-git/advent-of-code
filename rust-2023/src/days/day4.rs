use rust_utils::utils;

fn sum_card_pile_points(input: &Vec<String>) -> i32 {
	let mut total_points = 0;

	for l in input {
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
				if winning_nums.contains(&num) {
					matches += 1;
				}
			}
			if matches > 0 {
				total_points += i32::pow(2, matches - 1);
			}
		}
	}
	return total_points;
}

/// https://adventofcode.com/2023/day/4
pub fn main() {
	let input = utils::get_input(file!(), None);
	let mut t = utils::build_timer(file!());
	// PART ONE
	println!("The pile of cards is worth {} points", sum_card_pile_points(&input));
	t.step("part 1");

	// PART TWO
	t.step("part 2");
	t.total(file!());
}
