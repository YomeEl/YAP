#ifndef HASHSET_H
#define HASHSET_H

template <typename T>
class HashSet
{
public:
    HashSet() : _size(1), _count(0) { _arr = new T[1]; }
    HashSet(T arr[], size_t arrSize) : _size(arrSize), _count(arrSize)
    {
        _arr = new T[arrSize];
        for (size_t i = 0; i < arrSize; i++) _arr[i] = arr[i];
    }

    ~HashSet() { delete[] _arr; }

    void append(const T& item) 
    {
        if (Contains(item)) return;

        if (_count == _size) grow();
        _arr[_count++] = item;
    }
    void remove(const T& item)
    {
        for (size_t i = 0; i < _count; i++)
            if (_arr[i] == item) { remove(i); return; }
    }

    HashSet<T> Union(const HashSet<T>& other) const
    {
        auto res = copy();
        for (size_t i = 0; i < other._count; i++) res.append(other._arr[i]);
        return res;
    }
    HashSet<T> Except(const HashSet<T>& other) const
    {
        auto res = copy();
        for (size_t i = 0; i < other._count; i++) res.remove(other._arr[i]);
        return res;
    }
    HashSet<T> Intersect(const HashSet<T>& other) const
    {
        auto left = Except(other);
        auto right = other.Except(*this);
        auto all = left.Union(right);
        return Except(all);
    }
    bool Contains(const T& item) const
    {
        for (size_t i = 0; i < _count; i++)
            if (_arr[i] == item) return true;
        return false;
    }

    size_t count() { return _count; }
    T* toArray() const
    {
        T* res = new T[_count];
        for (size_t i = 0; i < _count; i++) res[i] = _arr[i];
        return res;
    }
    
private:
    HashSet(size_t size, size_t count) : _size(size), _count(count) { _arr = new T[size]; }
    void grow()
    {
        const size_t newSize = _size * 2;
        T* newArr = new T[newSize];
        for (size_t i = 0; i < _size; i++) newArr[i] = _arr[i];
        delete[] _arr;
        _arr = newArr;
        _size = newSize;
    }
    void remove(size_t idx)
    {
        for (size_t i = idx; i < _count - 1; i++) _arr[i] = _arr[i + 1];
        _count--;
    }
    HashSet<T> copy() const
    {
        HashSet<T> res(_size, _count);
        for (size_t i = 0; i < _count; i++) res._arr[i] = _arr[i];
        return res;
    }
    
private:
    size_t _size;
    size_t _count;
    T* _arr;
};

#endif // HASHSET_H