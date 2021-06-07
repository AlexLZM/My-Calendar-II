# My Calendar II

## Problem Description
Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

## Example
```
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation: 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
```

## Note

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].

## My solution strategy

**Binary search + dictionary**

Init: 
1. a sorted list for all start and end timestamps.
2. a dictionary mapping all timestamps to their counts
For each time interval [start, end) to book:
1. find the index of start and end timestamp in the sorted list by binary search (as i, j).
2. check any count in range [i, j) is greater or equal to 2, return false if so.
3. if start is not in the keys: set its count same as its last timestamp; return false if the count >= 2; insert the start time to the sorted list. (Increment j by 1 after the insertion).
4. if end is not in the keys: set its count same as its last timestamp and insert it to the sorted list.
5. Increment all counts in range [i, j) by 1.
6. return True
7. update all counts in range[i, j]
