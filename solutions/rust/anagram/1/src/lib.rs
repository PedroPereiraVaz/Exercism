use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    println!("WORD: '{}'", word);

    let mut results = HashSet::new();

    let word_lower = word.to_lowercase();
    
    let mut chars_word: Vec<char> = word_lower.chars().collect();
    chars_word.sort_unstable();
    
    for &candidate in possible_anagrams {
        println!("CANDIDATE: {}", candidate);

        let candidate_lower = candidate.to_lowercase();

        if candidate_lower.chars().count() != word_lower.chars().count() {
            println!("[ERROR] No coincide la cantidad de letras '{}'", candidate);
            continue;
        }
        
        if candidate_lower == word_lower {
            println!("[ERROR] El candidato no puede ser igual a la palabra original '{}'", candidate);
            continue;
        }

        let mut chars_candidate: Vec<char> = candidate_lower.chars().collect();
        chars_candidate.sort_unstable();

        if chars_candidate == chars_word {
            results.insert(candidate);
        }   
    }
    results
}
