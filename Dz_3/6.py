""" Сложность алгоритма O(log(n)). Сделаем два счетчика быстры и медленный. Быстрый будет двигаьтся через вершину,
а медленный по каждой вершине. Таким образом рано или чуть позднее быстрый догонит медленного, если список замкнут."""


def hasCycle(head):
    slow, fast = head, head
    while fast != None and fast.next != None:  # Условие на проверку существования fast.next.next
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
