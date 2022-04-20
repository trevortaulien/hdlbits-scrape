module top_module ( input clk, input d, output q );
​
    wire q1, q2;
    
    my_dff stage1( .clk(clk), .d(d), .q(q1) );
    my_dff stage2( .clk(clk), .d(q1), .q(q2) );
    my_dff stage3( .clk(clk), .d(q2), .q(q) );
    
endmodule
​
