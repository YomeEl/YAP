#ifndef DICTIONARY_H
#define DICTIONARY_H

#include <stddef.h>

template <typename K, typename V, size_t MaxKeys>
class Dictionary
{
public: 
    struct pair { K key = K(); V value = V(); bool valid = false; };

public:
    Dictionary() {};

    void append(const K& key, const V& value)
    {
        if (_count == MaxKeys) throw "Failed to append value: dictionary is full!";
        size_t position = pos(key);
        _arr[position].key = key;
        _arr[position].value = value;
        _arr[position].valid = true;
        _count++;
    }
    void remove(const K& key) { _arr[pos(key)].valid = false; _count--; }
    V& at(const K& key) { return _arr[pos(key)].value; }
    bool exists(const K& key) { return _arr[pos(key)].valid; }
    V& operator[](const K& key) { return at(key); }
    pair* pairs() const
    {
        if (_count == 0) return nullptr;
        pair* result = new pair[_count];
        size_t idx = 0;
        for (size_t i = 0; i < MaxKeys; i++)
            if (_arr[i].valid) result[idx++] = _arr[i];
        return result;
    }
    size_t count() const { return _count; }

private:
    static int hash(const K& key)
    {
        const unsigned char *buffer = reinterpret_cast<const unsigned char *>(&key);
        size_t bufferSize = sizeof(key);
        int sum = 0;
        for (size_t byte = 0; byte < bufferSize; byte++) sum += *(buffer + byte);
        return sum;
    }
    static size_t resolveCollision() { return 1; }
    size_t pos(const K& key, size_t shift = 0) const 
    { 
        if (shift >= MaxKeys) throw "Failed to append value: unresolvable collision!";
        size_t position = (hash(key) + shift) % MaxKeys;
        if (_arr[position].valid && _arr[position].key != key) 
            return pos(key, shift + resolveCollision()); 
        return position;
    };

private:
    pair _arr[MaxKeys];
    size_t _count = 0;
};

#endif // DICTIONARY_H