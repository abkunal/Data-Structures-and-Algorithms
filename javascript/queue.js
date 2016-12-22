/* Implementation of Queue Data Structure */

class Queue {
	/* Queue is a FIFO (first in, first out) data structure.
	 * Element added first will also be removed first.
	 */
	
	// initialize queue
	constructor() {
		this._storage = {};
		this._MAX = 20;
		this._start = -1;
		this._end = -1;
	}
	
	// add item to the queue
	enqueue( value ) {
		if ( this._end >= this._MAX - 1 ) {
			console.log( "Queue is Full!" );
			return false;
		}

		if ( this._start == -1 ) {
			this._start++;
		}
		this._end++;
		this._storage[this._end] = value;
		return true;
	}
	
	// removes an item from the start of queue
	dequeue() {
		if ( this.size() >= 1 ) {
			let nextUp = this._storage[this._start];
			delete this._storage[this._start];

			if ( this._start == this._end ) {
				this._start = this._end = -1;
			}
			else {
				this._start++;
			}
			return nextUp;
		}
		else {
			console.log("Queue is Empty!");
			return false;
		}
	}
	
	// calculate size of the queue
	size() {
		if ( this._start == -1 && this._end == -1 ) {
			return 0;
		}
		else if ( this._start == this._end ) {
			return 1;
		}
		else {
			return this._end - this._start + 1;
		}
	}
}
