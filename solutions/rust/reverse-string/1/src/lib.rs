pub fn reverse(input: &str) -> String {
    let input_reversed: String = input
        .chars()
        .rev()
        .collect();
    return input_reversed;
}
