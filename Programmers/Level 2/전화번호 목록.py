def solution(phone_book):
    phone_book.sort()
    
    min_word = phone_book.pop(0)
    phone_book = [phone[:len(min_word)] for phone in phone_book]
    
    if min_word in phone_book:
        return False
    else:
        return True
        