import * as CryptoJS from "crypto-js";
class Block {

    public index : number; // block index
    public hash : string; // block hash (hash는 모든 속성을 엄청 길고 수학적으로 이상한 하나의 문자열로 결합한 것이다.)
    public previous_hash : string; // previous hash
    public data : string; // block data
    public timestamp : number; // block timestamp

    static calculateBlockHash = ( // class 안에 calculataBlockHash라는 static 메소드 선언
                                    // calculateBlockHash 메소드는 Block 클래스 안에 있고, 
                                    // static으로 선언되었기 때문에 클래스가 생성되지 않았어도 호출할 수 있는 메소드이다.

        index: number, // index의 타입을 number로 지정
        previous_hash: string, // previous_hash의 타입을 string으로 지정
        data: string, // data의 타입을 string로 지정
        timestamp: number // timestamp의 타입을 number로 지정
        
        ): string => CryptoJS.SHA256(index + previous_hash + data + timestamp).toString(); // 리턴값은 CryptoJS.SHA256이다. 
                                                                                // 그리고 그 리턴 값을 string으로 변환한다.

    constructor(

        index: number, // index의 타입을 number로 지정
        hash: string, // hash의 타입을 string으로 지정
        previous_hash: string, // previous_hash의 타입을 string으로 지정
        data: string, // data의 타입을 string으로 지정
        timestamp: number // timestamp의 타입을 number로 지정

    ) { // 생성자 (인자 : index, hash, previous_hash, data, blockstamp)

        this.index = index; // 같은 속성의 이름을 준다. (즉, 해당 클래스의 index는 생성자의 index와 같다는 것이다.)
        this.hash = hash; // 같은 속성의 이름을 준다. (즉, 해당 클래스의 hash는 생성자의 hash와 같다는 것이다.)
        this.previous_hash = previous_hash; // 같은 속성의 이름을 준다. (즉, 해당 클래스의 previous_hash는 생성자의 previous_hash와 같다는 것이다.)
        this.data = data; // 같은 속성의 이름을 준다. (즉, 해당 클래스의 data는 생성자의 data와 같다는 것이다.)
        this.timestamp = timestamp; // 같은 속성의 값을 준다. (즉, 해당 클래스의 timestamp는 생성자의 timestamp와 같다는 것이다.)

    }

}

const harusterBlock: Block = new Block(0, "2020202010100", "", "Hello", 124000);

let Blockchain: Block[] = [harusterBlock];// Blockchain = 블록의 연결

const getBlockchain = () : Block[] => Blockchain; // getBlockchain함수는 Block배열을 리턴한다. (Blockchain 변수 리턴)

const getLatestBlockchain = () : Block => Blockchain[Blockchain.length - 1]; // getLatestBlockchain함수는 Block을 리턴한다. 
                                                                            // 블록 안에서 가장 최근 값을 준다.

const getNewTimeStamp = (): number => Math.round(new Date().getTime() / 1000); // getNewTimeStamp는 number를 리턴값으로 갖는다.

console.log(Blockchain);

export {};