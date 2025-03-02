#ifndef LINKEDLIST_H
#define LINKEDLIST_H

template <typename T>
struct LinkedListItem
{
    T value;
    LinkedListItem<T> *next = nullptr;
    LinkedListItem<T> *prev = nullptr;
};

template <typename T>
class LinkedList
{
public:
    LinkedList() {}
    LinkedList(T arr[], size_t arrSize) 
    {
        for (size_t i = 0; i < arrSize; i++) append(arr[i]);
    }
    
    ~LinkedList()
    {
        LinkedListItem<T> *cur = _root;
        while (cur) 
        { 
            LinkedListItem<T> *next = cur->next;
            delete cur;
            cur = next;
            if (cur == _root) return;
        }
    }

    LinkedListItem<T>* first() const { return _root; }
    LinkedListItem<T>* last() const { return _last; }

    void append(const T &value)
    {
        LinkedListItem<T> *item = new LinkedListItem<T> { value, nullptr, nullptr };
        if (!_last) { _root = item; _last = item; }
        else 
        { 
            _last->next = item; 
            item->prev = _last;
            _last = item; 
        }
    }
    void remove(const T &value)
    {
        LinkedListItem<T> *cur = _root;
        while (cur) 
        {
            LinkedListItem<T> *next = cur->next;
            if (cur->value == value) remove(cur); 
            cur = next;
            if (cur == _root) break;
        }
    }

    LinkedListItem<T>* find(const T &value)
    {
        LinkedListItem<T> *cur = _root;
        while (cur) 
        {
            if (cur->value == value) return cur;
            cur = cur->next;
            if (cur == _root) break;
        }
        return nullptr;
    }

private:
    void remove(LinkedListItem<T> *cur)
    {
        if (!cur) return;

        if (!cur->prev)
            _root = cur->next;
        else
            cur->prev->next = cur->next;

        if (!cur->next)
            _last = cur->prev;
        else
            cur->next->prev = cur->prev;
            
        delete cur;
    }

private:
    LinkedListItem<T> *_root = nullptr;
    LinkedListItem<T> *_last = nullptr;
};

#endif // !LIST_H
