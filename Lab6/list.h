#ifndef LIST_H
#define LIST_H

template <typename T>
struct ListItem
{
    T value;
    ListItem<T> *next = nullptr;
};

template <typename T>
class List
{
public:
    List() {}
    List(T arr[], size_t arrSize) 
    {
        for (size_t i = 0; i < arrSize; i++) append(arr[i]);
    }
    
    ~List()
    {
        ListItem<T> *cur = _root;
        while (cur) 
        { 
            ListItem<T> *next = cur->next;
            delete cur;
            cur = next;
            if (cur == _root) return;
        }
    }

    ListItem<T>* first() const { return _root; }
    ListItem<T>* last() const { return _last; }

    ListItem<T>* append(const T &value)
    {
        ListItem<T> *item = new ListItem<T> { value, nullptr };
        if (!_last) { _root = item; _last = item; return item; }
        else { _last->next = item; _last = item; }
        return item;
    }
    void remove(const T &value)
    {
        ListItem<T> *cur = _root, *prev = nullptr;
        while (cur) 
        {
            if (cur->value == value) remove(prev, cur);
            prev = cur; cur = cur->next;
        }
    }
    void remove(const ListItem<T> * const item)
    {
        ListItem<T> *cur = _root, *prev = nullptr;
        while (cur) 
        {
            if (cur == item) remove(prev, cur);
            prev = cur; cur = cur->next;
        }
    }

    ListItem<T>* find(const T &value)
    {
        ListItem<T> *cur = _root;
        while (cur) 
        {
            if (cur->value == value) return cur;
            cur = cur->next;
        }
        return nullptr;
    }

private:
    void remove(ListItem<T> *prev, ListItem<T> *cur)
    {
        if (!cur) return;

        if (!prev)
            _root = cur->next;
        else
            prev->next = cur->next;

        if (_last == cur) _last = prev;
        delete cur;
    }

private:
    ListItem<T> *_root = nullptr;
    ListItem<T> *_last = nullptr;
};

#endif // !LIST_H
