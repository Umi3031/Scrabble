#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <time.h>

#define HAND_SIZE 10
#define WORDLIST_FILENAME "C:\\Users\\user\\Downloads\\hangman\\words.txt"
#define RECORD_FILENAME "record.txt"

const char VOWELS[] = "aeiou";
const char CONSONANTS[] = "bcdfghjklmnpqrstvwxyz";

int SCRABBLE_LETTER_VALUES[26] = {
    1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10
};

typedef struct {
    char letter;
    int count;
} Hand;

void display_hand(Hand hand[], int size) {
    int i=30;
    printf("\033[%dm Tanii useguud: ",i+3);
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < hand[i].count; j++) {
            printf("%c ", hand[i].letter);
        }
    }
    printf("\n");
}

void deal_hand(Hand hand[], int *size) {
    int num_vowels = (int)ceil(HAND_SIZE / 3.0);
    *size = 0;
    
    hand[*size].letter = '*';
    hand[*size].count = 1;
    (*size)++;
    
    for (int i = 1; i < num_vowels; i++) {
        hand[*size].letter = VOWELS[rand() % strlen(VOWELS)];
        hand[*size].count = 1;
        (*size)++;
    }
    
    for (int i = num_vowels; i < HAND_SIZE; i++) {
        hand[*size].letter = CONSONANTS[rand() % strlen(CONSONANTS)];
        hand[*size].count = 1;
        (*size)++;
    }
}

int get_word_score(const char *word) {
    int score = 0, length = strlen(word);
    for (int i = 0; word[i] != '\0'; i++) {
        score += SCRABBLE_LETTER_VALUES[tolower(word[i]) - 'a'];
    }
    if (length >= HAND_SIZE) {
        score += 50;
    }
    return score;
}

int is_valid_word(const char *word, Hand hand[], int size) {
    int letter_counts[26] = {0};
    for (int i = 0; i < size; i++) {
        letter_counts[hand[i].letter - 'a'] += hand[i].count;
    }
    
    if (strlen(word) < 3) { // 3 үсэг байх шаардлагатай
        return 0;
    }
    
    for (int i = 0; word[i] != '\0'; i++) {
        if (letter_counts[tolower(word[i]) - 'a'] == 0) {
            return 0;
        }
        letter_counts[tolower(word[i]) - 'a']--;
    }
    return 1;
}

void update_hand(Hand hand[], int *size, const char *word) {
    for (int i = 0; word[i] != '\0'; i++) {
        for (int j = 0; j < *size; j++) {
            if (hand[j].letter == tolower(word[i]) && hand[j].count > 0) {
                hand[j].count--;
                if (hand[j].count == 0) {
                    for (int k = j; k < *size - 1; k++) {
                        hand[k] = hand[k + 1];
                    }
                    (*size)--; // Useg ustgakh
                }
                break;
            }
        }
    }
}

void save_high_score(int score) {
    FILE *file = fopen(RECORD_FILENAME, "a");
    if (file) {
        fprintf(file, "%d\n", score);
        fclose(file);
    }
}

int get_high_score() {
    FILE *file = fopen(RECORD_FILENAME, "r");
    if (!file) return 0;
    int high_score = 0, temp;
    while (fscanf(file, "%d", &temp) != EOF) {
        if (temp > high_score) {
            high_score = temp;
        }
    }
    fclose(file);
    return high_score;
}

int main() {

    srand(time(NULL));
    
    Hand hand[HAND_SIZE];
    int size;
    deal_hand(hand, &size);
    display_hand(hand, size);
    
    char word[50];
    int total_score = 0;
    int valid_word_count = 0;
    int i=30;
    
    while (size>2) {
        printf("\033[%dm Zokhison ugee oruulna uu: ",i+4);
        scanf("%s", word);
        
        if (is_valid_word(word, hand, size)) {
            int score = get_word_score(word);
            printf("\033[%dm Sain baina! Tanii onoo: %d\n",i+2, score);
            total_score += score;
            save_high_score(score);
            update_hand(hand, &size, word);
            display_hand(hand, size);
            valid_word_count++;
        } else {
            printf("\033[%dm Buruu ug baina! Ugs utagagdlaa.\n",i+1);
        }
        
        if (valid_word_count == 10) {
            printf("\033[%dm Ta khamgiin ikhdee 10 ug zohioh bolomjtoi.",i+4);
            printf("\033[%dm Tanii niit onoo: %d\n",i+2, total_score);
        }
    }
    
    printf("\033[%dm Onoonii khamgiin deed record: %d\n",i+3, get_high_score());
    printf("\033[%dm Husbel ta record ebdej bolno",i+4);
    return 0;
}
