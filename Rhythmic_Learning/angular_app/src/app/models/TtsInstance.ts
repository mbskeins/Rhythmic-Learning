export class TtsInstance {
    public text: string;
    public delay: number;

    constructor(text: string, delay: number){
        this.text = text;
        this.delay = delay;
    }
}